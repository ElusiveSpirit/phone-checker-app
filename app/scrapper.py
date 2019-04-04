import re

import requests
from bs4 import BeautifulSoup

PHONE_REGEX = re.compile(
    '^(\\+7|7|8)?[\\s\\-]?\\(?[489][0-9]{2}\\)?[\\s\\-]?[0-9]{3}[\\s\\-]?[0-9]{2}[\\s\\-]?[0-9]{2}$')


def clean_number(number: str) -> str:
    """
    Format and clean phone number from string

    :param number: Dirty phone number
    :return: Clean number in 8KKKNNNNNNN format
    """
    cleaned_number = ''.join(filter(lambda x: x.isdigit(), number))
    if cleaned_number[0] == '7':
        cleaned_number = f'8{cleaned_number[1:]}'
    return cleaned_number


def find_phones(contacts_page_url: str) -> list:
    """
    Find phones on the web page

    :param contacts_page_url: Url with contacts list to find phones
    :return: List with found phone number
    """
    r = requests.get(contacts_page_url)
    soup = BeautifulSoup(r.text, features='lxml')

    number_list = []
    for text in soup.find_all(text=PHONE_REGEX):
        cleaned_phone = clean_number(text)
        if cleaned_phone not in number_list:
            number_list.append(cleaned_phone)

    return number_list
