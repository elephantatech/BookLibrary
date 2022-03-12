# Testing

this document is for how to run unit tests within this application

## Python

we are using pytest with coverage to run the python tests

To test models enter the following commands
```bash
booklibrary> cd fastapi-backend 
fastapi-backend> pytest --cov=models tests -vv
```

Test all files in fastapi backend dir
```bash
booklibrary> cd fastapi-backend 
fastapi-backend> pytest --cache-clear --cov=. --cov-report=term --cov-fail-under=80 tests -vv
```