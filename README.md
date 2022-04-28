### to install project
```
pip install -e .
```
or
```
pip install -e .'[dev]'
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


### Known issues
- in python shell db is not getting detected (python >> froom run import app, db >>db gives <SQLAlchemy engine=None>)