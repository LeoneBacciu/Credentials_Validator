from Validators import PasswordValidator
from Validators import Validator

if __name__ == "__main__":
    user = PasswordValidator([4], [1], [0], [1], [0], {'username': 'cicciO02'})
    print(user.verify('cicciO02'))
