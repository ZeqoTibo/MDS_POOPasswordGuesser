class SpecialChar:
    _array = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|']

    @classmethod
    def get_special_characters(cls):
        return cls._array
