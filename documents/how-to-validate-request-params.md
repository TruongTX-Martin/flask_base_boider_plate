## What is request params validation?

**Request params validation** is a action to validate the params in request for sure them are met expectations, and prevent invalid data befor continue to process.


## How to use?

#### 1. Define the params must be validate in the request

Example: with the sign in feature, you need to validate `email` & `password`

#### 2. Create the schema file 

Create a schema file to define rules for validating the params.

Example: `app/views/api/schemas/login_input_schema.py`
```
from marshmallow import fields
from .base_schema import BaseSchema

class LoginInputSchema(BaseSchema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
```
[More fields references](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#module-marshmallow.fields)


#### 3. Add schema to controller function to validate the request params
```
...
# import the defined schema above
from app.views.api.schemas import LoginInputSchema
...

# use in sigin feature
def signin(user_service: UserService):
    # get request data
    request_data = request.get_json()

    # validate request data by the schema was defined
    LoginInputSchema().load(request_data)

    # get the input data after validating
    input_data = {
        'email': request_data['email'],
        'password': request_data['password']
    }

    # use validated data for login action
    user = user_service.login(**input_data)
    return Token(user).response()
```

[Reference](https://marshmallow.readthedocs.io/en/stable/examples.html)