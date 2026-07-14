# Termux Android Gateway Agent

## Pré-requisitos

- Android com chip SIM e créditos.
- Termux instalado.
- App Termux:API instalado.

## Instalar

```bash
pkg install git
git clone <REPOSITORIO>
cd sms-gateway-platform/termux-agent
bash install.sh
```

Edite `config.json` e coloque a URL do backend Render.

## Rodar

```bash
./start.sh
```

## Comandos

```bash
python main.py status
python main.py logs
python main.py info
python main.py test +5511999999999 "Teste"
python main.py docs
python main.py restart
```
