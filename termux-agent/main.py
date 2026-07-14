import json
import time
import typer
from rich.console import Console
from rich.panel import Panel
from api import ApiClient
from device import model, battery, gateway_id
from sms import send_sms
from logger import log, tail

app = typer.Typer(help='SMS Gateway Node CLI')
console = Console()
sent = 0


def cfg():
    data = json.load(open('config.json'))
    if data.get('gateway_id') == 'gateway-android-001':
        data['gateway_id'] = gateway_id()
        json.dump(data, open('config.json', 'w'), indent=2)
    return data


@app.command()
def start():
    global sent
    c = cfg()
    api = ApiClient(c['api_url'])
    gid = c['gateway_id']
    name = c.get('name') or model()
    console.print(Panel.fit(f"SMS GATEWAY NODE\nGateway: {name}\nStatus: ONLINE\nAPI: {c['api_url']}", style='green'))
    api.post('/gateway/register', {'gateway_id': gid, 'name': name, 'model': model(), 'battery': battery()})
    while True:
        api.post('/gateway/heartbeat', {'gateway_id': gid, 'battery': battery(), 'sent_count': sent})
        tasks = api.get('/queue/tasks', {'gateway_id': gid, 'limit': 5}).get('tasks', [])
        for task in tasks:
            ok, err = send_sms(task['number'], task['message'])
            sent += 1 if ok else 0
            api.post('/queue/complete', {'task_id': task['id'], 'gateway_id': gid, 'status': 'SENT' if ok else 'FAILED', 'error': err})
            log(f"{task['number']} {'SENT' if ok else 'FAILED'} {err or ''}")
        time.sleep(c.get('poll_seconds', 5))


@app.command()
def status():
    c = cfg()
    console.print(Panel.fit(f"Gateway: {c['gateway_id']}\nAPI: {c['api_url']}\nBateria: {battery()}%"))


@app.command()
def logs():
    console.print(tail())


@app.command()
def info():
    status()


@app.command()
def test(number: str, message: str = 'Teste SMS Gateway'):
    console.print(send_sms(number, message))


@app.command()
def docs():
    console.print(open('../docs/TERMUX.md').read())


@app.command()
def restart():
    start()


if __name__ == '__main__':
    app()
