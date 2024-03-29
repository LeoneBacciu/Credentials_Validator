# Account credentials checker

This package takes care of verifing the credentials serverside.

## Download
You can `pip install` by
```commandline
pip3 install Credentials-Validator
```

## Usage

You can import the pakage by typing

```python
from Credentials_Validator import UsernameValidator, PasswordValidator
```
\
The general usage is:

```python
from Credentials_Validator import UsernameValidator

user = UsernameValidator([4], # length range
                         [1], # number of lower-case chars range
                         [1], # number of upper-case chars range
                         [1,3], # number of numbers range
                         [0,0], # number of symbols range
                         )
```
\
The use of range is:

```python
[2, 5] # minimum 2, maximum 5 characters
[1] # at least one
[0] # not necessary, not denied
[0, 4] # not necessary, maximum 4 characters
[0, 0] # denied
```

### Validation
In order to validate a `text` (Username or password) you have to call the method `Validator.verify(text)`.\
It returns two objects:
1. a `boolean` (`True` if the text is valid, `False` if there is one or more errors)
2. a `string`, that can be:
    * `''` empty, if there are no errors
    * `'length'` if the `text` is too short or too long
    * `'lower'` if there are too few or too many lower-case characters
    * `'upper'` if there are too few or too many upper-case characters
    * `'digit'` if there are too few or too many numbers
    * `'symbols'` if there are too few or too many allowed symbols
```python
from Credentials_Validator import UsernameValidator

user = UsernameValidator([4, 10], [1], [2], [0], [1],)

is_valid, error = user.verify('PasswOrd!')
print((is_valid, error))
#returns (True, '')

is_valid, error = user.verify('PasswOrd3')
print((is_valid, error))
#returns (False, 'symbols')

is_valid, error = user.verify('Password!')
print((is_valid, error))
#returns (False, 'upper')

is_valid, error = user.verify('th1sPasswOrdist00long')
print((is_valid, error))
#returns (False, 'length')
```

## Differences between UsernameValidator and PasswordValidator

### UsernameValidator
The `UsernameValidator` comes with a special argument called `django_model`.\
It can be used to automatically check if the username is already taken in the Django User model, if it is taken, it will return the error `'existing'`\
In this example the default User model is passed:
```python
from django.contrib.auth.models import User
from Credentials_Validator import UsernameValidator

user = UsernameValidator([4,10], [1], [1], [2], [0,0], django_model=User)
```
If you are using a custom Django User model:
```python
from django.contrib.auth import get_user_model
from Credentials_Validator import UsernameValidator

user = UsernameValidator([4,10], [1], [1], [2], [0,0], django_model=get_user_model())
```

### PasswordValidator
The `PasswordValidator` comes with a special argument called `username`.\
It checks if the password is the same as the username, in which case it returns the `'equal'` error.\
```python
from Credentials_Validator import PasswordValidator

username = 'myusername'

password = PasswordValidator([8,12], [2], [2], [2], [1], username=username)
```
## Extra features

### Customization
\
The default symbols are: `!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`.\
\
You can customize the simbols by passing your custom list (string) as a keyword argument:

```python
from Credentials_Validator import UsernameValidator

my_symbols = '!?$%&@#'

user = UsernameValidator([4, 10], [1], [1], [0], [1], symbols_list=my_symbols)
```

### Inheritance
You can add your custom verification function by inheriting the `Validator` class and overriding the `__init__` method to add keyword arguments and `extra_validation` one to add your validatin function.\
The `__init__` should look like this:
```python
from Credentials_Validator import Validator

class MyValidator(Validator):

    def __init__(self, length, chars, Chars, nums, symbols, **kwargs):
        super().__init__(length, chars, Chars, nums, symbols, **kwargs) # DON'T EDIT THIS!

        self.myargument = kwargs.get('mykeyword', None) # Edit 'myargument' and 'mykeyword'
``` 
The `extra_validation` should return `None` if the `text` is valid, if it is not, `False` and `myerrormessage` (can be anything)
```python
    def extra_validation(self, text): # text is the .verify() argument
        if self.myargument in text: # can be any condition
            return False, 'myerror'
        return None
```
