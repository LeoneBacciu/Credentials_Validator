# Account credentials checker

This package takes care of verifing the credentials serverside.

##Download
You can pip install by
```commandline
pip3 install Credentials-Validator
```

##Usage

You can import the pakage by typing

```python
from Credentials_Validator import UsernameValidator, PasswordValidator
```

The general use is:

```python
from Credentials_Validator import UsernameValidator
user = UsernameValidator([4], #length
                         [1], #lower-case chars range
                         [1], #upper-case chars range
                         [1], #numbers range
                         [0], #symbols range
                         symbols_list='')
```