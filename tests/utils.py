
class MockResponse:
    def __init__(self, mock_file_name):
        with open(f'./mocks/{mock_file_name}', 'rb') as f:
            self.text = f.read().decode('utf-8')
            self.status_code = 200

    def text(self):
        return self.text
