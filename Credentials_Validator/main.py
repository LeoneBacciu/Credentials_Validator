from Validators import PasswordValidator
from Validators import Validator

if __name__ == "__main__":
    user = PasswordValidator([4],
                             [0,0],
                             [1],
                             [1],
                             [0],
                             {'username': 'cicciO03'})
    print(user.verify('ciccio'))
