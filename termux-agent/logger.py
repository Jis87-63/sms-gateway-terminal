from pathlib import Path
from datetime import datetime

LOG = Path('agent.log')


def log(msg):
    line = f"{datetime.utcnow().isoformat()} {msg}"
    print(line)
    with LOG.open('a') as handle:
        handle.write(line + '\n')


def tail():
    return LOG.read_text() if LOG.exists() else 'Sem logs ainda.'
