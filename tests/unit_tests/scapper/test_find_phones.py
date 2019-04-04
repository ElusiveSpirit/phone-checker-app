from pytest_mock import MockFixture

from app.scrapper import find_phones
from tests.utils import MockResponse


def test_find_single_phone_in_hands(mocker: MockFixture):
    get_mock = mocker.patch('requests.get')
    get_mock.return_value = MockResponse('hands.html')

    numbers = find_phones('https://hands.ru/company/about')

    assert numbers == ['84951377767']


def test_find_single_phone_in_repetitors(mocker: MockFixture):
    get_mock = mocker.patch('requests.get')
    get_mock.return_value = MockResponse('repetitors.html')

    numbers = find_phones('https://repetitors.info/')
    assert numbers == ['84955405676', '88005555676', '88005057283', '88005057284']


def test_find_single_phone_in_agro24(mocker: MockFixture):
    get_mock = mocker.patch('requests.get')
    get_mock.return_value = MockResponse('agro24.html')

    numbers = find_phones('https://agro24.ru/product/voda-optom/')
    assert numbers == ['84951210000', '88007752388']
