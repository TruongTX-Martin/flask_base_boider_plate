# Authentication
Let’s say you have a Flask application that allows user to add tweets.
Each tweet belongs to a user and only logged in user can add tweet. 
Therefore you want to limit some routes to only logged in users and if user is not logged in, 
they will be redirected to the login page

Adding the login check for every route is quite cumbersome and violates the DRY principle.
It would be very handy if we can just decorate such routes with @login_required and all the login checks will be done automatically


Authentication use pyjwt `https://github.com/jpadilla/pyjwt`

The authentication we are using decorator.

Check http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
to see detail about decorator


## Login
```python
@app.route("/signin", methods=["POST"])
@inject
def signin(user_service: UserService):
    request_data = request.get_json()
    LoginInputSchema().load(request_data)
    input_data = {
        'email': request_data['email'],
        'password': request_data['password']
    }

    user = user_service.login(**input_data)
    return Token(user).response()
```

### Workflow:
->signin get data email and password from request
```python
request_data = request.get_json()
    LoginInputSchema().load(request_data)
    input_data = {
        'email': request_data['email'],
        'password': request_data['password']
    }
```
-> call user service login `user = user_service.login(**input_data)`

-> Service login check user name and password is correct or not
```python
user = self.user_repository.get_user_by_email(email)
if user is None:
    raise APIResponseError('Incorrect username.')
elif not user.check_password(password):
    raise APIResponseError('Incorrect password.')

session.clear()
session['user_id'] = user.id
```
The session helpful when in case weblogin, not API

->Return Token `return Token(user).response()`
 
In Token response class, model `User encoded using decorate` and return token field like this
```json
{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNTkyNTU2MTI1fQ.qHNUlV-UawMFqxt_jRHRsD6dgDyXhwhnHHelYDSa4r4"}
```


## Use Token

- Add `@token_required` before each function required login
```python
@app.route('', methods=["GET"])
@inject
@token_required
def me():
    user = g.user
    return User(model=user).response(), 200
```

### Workflow
 -> After add `@token_required`, each request to server, the function `decorator` will be run
 Check header, get user and set global variable `g.user  = user`
 `user = g.user` in controller get the current user and return User response


## How it work?

Currently we created function `token_required` in `app/middlewares/authenticate.py`

1. First Check the Authorization in header request:
 `auth_header = request.headers.get('Authorization')`

2. Second Get the token: ` _, token = auth_header.split()`

3. Third decode the token, we get the user id `decoded = jwt.decode(token, Config.SECRET_KEY, algorithms='HS256')`

4. Four get user and set user by user service
`user_service.load_logged_in_user_to_request(decoded['id'])`

When use login, system use pyjwt to generate a token by exp (expired time),
user id, and SECRET_KEY with HS256 

When use send token in header, system decode and get the user id

Frontend:
- Add header: `Authorization Bearer TokenKey`

![Accesstoken](images/access-token-in-header.png)