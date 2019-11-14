# python_frameworks flask_demo

## Launch app

```bash
source ./venv/bin/activate
python manage.py
```

## Tests api

```bash
curl http://localhost:8000/api/test
{
    "code": -1, 
    "data": {}
}

curl http://localhost:8000/api/test -d "id=1"
{
    "code": 0, 
    "data": {
        "id": 1
    }
}
```
