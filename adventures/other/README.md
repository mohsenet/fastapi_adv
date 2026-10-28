See the endpoints of FastAPI
```bash
http://192.168.129.106:8000/docs
```
```bash
http://192.168.129.106:8000/redoc
```
```bash
http://192.168.129.106:8000/openapi.json
```
```bash
curl -s http://192.168.129.106:8000/openapi.json | python -m json.tool | grep '"\+"' | head -50
```
```bash
curl -s http://192.168.129.106:8000/openapi.json \
  | python -c "import sys,json;d=json.load(sys.stdin);[print(m.upper(),p) for p,v in d['paths'].items() for m in v if m in ('get','post','put','delete','patch')]"
```

