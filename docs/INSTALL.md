# Instalação

## Backend

1. Configure um projeto Firebase Realtime Database.
2. Gere uma service account e defina `FIREBASE_SERVICE_ACCOUNT=/caminho/arquivo.json`.
3. Instale dependências e rode a API:

```bash
cd backend
pip install -r requirements.txt
PYTHONPATH=. uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Dashboard

```bash
cd dashboard
npm install
VITE_API_URL=https://sua-api.onrender.com npm run build
```

## Termux

```bash
pkg install git
git clone <REPOSITORIO>
cd sms-gateway-platform/termux-agent
bash install.sh
```
