class Validator:

    def __init__(self, length, chars, Chars, nums, symbols, *args, **kwargs):

        self.text = ''
        self.length = length
        if len(self.length) < 2:
            self.length.append(float('inf'))
        self.chars = chars
        self.Chars = Chars
        self.nums = nums
        self.symbols = symbols
        self.symbols_list = kwargs.get('symbols_list', [s for s in '@#$%/£!?'])
        self.extra = self.__safe_get(args, 0, {})

    @staticmethod
    def __safe_get(l, index, default):
        try:
            return l[index]
        except IndexError:
            return default

    def __check(self, func, limit):
        if limit:
            chars = 0
            for char in self.text:
                chars += 1 if func(char) else 0
            return not limit[0] <= chars <= self.__safe_get(limit, 1, self.length[1])
        return False

    def extra_validation(self, text):
        return None

    def verify(self, text: str):
        self.text = text

        extra = self.extra_validation(self.text)
        if extra:
            return extra

        if not self.length[0] <= len(self.text) <= self.length[1]:
            return False, 'length'

        if self.__check(lambda c: c.islower(), self.chars):
            return False, 'lower'

        if self.__check(lambda c: c.isupper(), self.Chars):
            return False, 'upper'

        if self.__check(lambda c: c.isdigit(), self.nums):
            return False, 'digit'

        if self.__check(lambda c: c in self.symbols_list, self.symbols):
            return False, 'symbols'

        return True, ''


class UsernameValidator(Validator):
    def extra_validation(self, text):
        model = self.extra.get('django', None)
        if model:
            if model.objects.filter(username=text):
                return False, 'existing'


class PasswordValidator(Validator):

    def extra_validation(self, text):
        if text == self.extra.get('username', None):
            return False, 'equal'