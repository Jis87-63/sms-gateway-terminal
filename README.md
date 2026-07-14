# SMS Gateway Platform

Monorepo profissional para operar celulares Android com Termux, Termux:API e chip SIM como gateways distribuídos de envio SMS.

## Componentes

- `backend/`: API FastAPI para autenticação, gateways, campanhas, mensagens, filas, logs e estatísticas.
- `dashboard/`: painel administrativo React preparado para Vercel.
- `termux-agent/`: agente Python para Android/Termux com CLI Rich/Typer.
- `docs/`: documentação operacional.

## Instalação rápida

### Backend local

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=. uvicorn app.main:app --reload
```

Acesse `http://localhost:8000/docs`.

### Dashboard local

```bash
cd dashboard
npm install
VITE_API_URL=http://localhost:8000 npm run dev
```

### Termux Android

```bash
git clone <REPOSITORIO>
cd sms-gateway-platform/termux-agent
bash install.sh
nano config.json
./start.sh
```

## Deploy

- Render: use `backend/render.yaml` ou crie Web Service Docker apontando para `backend/`.
- Vercel: importe o repositório, defina Root Directory como `dashboard/` e configure `VITE_API_URL` com a URL do backend.

## API principal

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

## Segurança

Troque `ADMIN_PASSWORD`, `JWT_SECRET` e use uma conta de serviço Firebase em produção por meio da variável `FIREBASE_SERVICE_ACCOUNT`.
