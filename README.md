### to install project
```
pip install -e .
```
or
```
pip install -e .'[dev]'
```

```
pip install tox
```

### db operations
initialisation of db
```
flask db init
```
migrate the models using 
```
flask db migrate --message "add User model"
```
and then
```
flask db upgrade
```
### curl
```
curl -X 'POST' \
  'http://localhost:5000/api/v1/auth/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'email=user%40test.com&password=123456
```

### Known issues
- in python shell db is not getting detected (python >> froom run import app, db >>db gives <SQLAlchemy engine=None>)