# API

Base URL: `https://sua-api.onrender.com`

## Rotas

- `POST /login`
- `POST /gateway/register`
- `GET /gateway/list`
- `POST /gateway/heartbeat`
- `GET /gateway/status`
- `POST /message/create`
- `GET /message/list`
- `GET /message/status/{id}`
- `GET /queue/tasks`
- `POST /queue/complete`
- `POST /campaign/create`
- `GET /campaign/list`

## Exemplo Gateway

```json
{"gateway_id":"gateway-redmi-001","name":"Redmi 14C","model":"Android","battery":90}
```

`GET /queue/tasks?gateway_id=gateway-redmi-001&limit=5` bloqueia tarefas para o gateway, evitando duplicidade.
