# Code by ByungWook.Kang @lesimor


class Response:
    def __init__(self, data, error=None):
        self._data = data
        self._error = error

    def response(self):
        return {
            'result': self._data
        }
