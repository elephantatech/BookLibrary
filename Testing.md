# Testing

this document is for how to run unit tests within this application

## Python

we are using pytest with coverage to run the python tests

To test models enter the following commands
```bash
booklibrary> cd fastapi-backend 
fastapi-backend> pytest --cov=models tests -vv
```