## What is request validate?

**Request validate** is a middleware to validate the params in request for sure them are met expectations, and prevent invalid data befor continue to process.


## How to use?

#### In controller file 
```
...
from ....middlewares.request_validate import *    # import middleware
...


@app.route("/signin", methods=["POST"])
@inject
# add middleware
@request_validate(
    Param('email', 'JSON', str, rules=[Email()]),               # set params validate rule
    Param('password', 'JSON', str, rules=[MinLength(6)])        # set params validate rule
)
def signin(user_service: UserService, *params):
    request_data = request.get_json()
    LoginInputSchema().load(request_data)
    input_data = {
        'email': request_data['email'],
        'password': request_data['password']
    }

    user = user_service.login(**input_data)
    return Token(user).response()
...
```

## Add more rule

goto file `app/middlewares/validators/rules.py`

example
```
class Email(AbstractRule):

    def __init__(self):
        """
        :param str pattern:
        """
        self.pattern = re.compile(r'^[a-z][a-z0-9_\.]{0,32}@[a-z0-9]{2,}(\.[a-z0-9]{2,4}){1,2}$')

    def validate(self, value):
        errors = []
        if not self.pattern.search(value):
            errors.append('{} is not a email'.format(value))
        return errors
```