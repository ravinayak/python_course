class AuthorNotFoundException(ValueError):
    def __init__(self, message, code):
        self.code = code
        super().__init__(f' Error Code :: {code}, Message = {message}')

class TagNotFoundException(ValueError):
    def __init__(self, message, code):
        self.code = code
        super().__init__(f' Error Code :: {code}, Message :: {message}')
        
class QuoteNotFoundException(ValueError):
    def __init__(self, message, code):
        self.code = code
        super().__init__(f' Error Code :: {code}, Message :: {message}')