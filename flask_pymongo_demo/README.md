# python_frameworks flask_pymongo_demo

## Launch app

```bash
docker-compose up -d
source ./venv/bin/activate
python create_db.py
python app.py
```

## Tests app

```bash
curl http://localhost:8000/insert
{
  "data": "{\"_id\": \"5dc9068533944cc0685fe9bb\", \"id\": 1, \"online\": true}"
}

curl http://localhost:8000/list
{
  "data": "[{\"_id\": \"5dc9068533944cc0685fe9bb\", \"id\": 1, \"online\": true}]"
}
```
