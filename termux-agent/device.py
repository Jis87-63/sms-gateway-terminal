import json, subprocess, uuid

def sh(cmd):
    try: return subprocess.check_output(cmd, shell=True, text=True).strip()
    except Exception: return ""

def model(): return sh('getprop ro.product.model') or 'Android Termux'
def battery():
    raw=sh('termux-battery-status')
    try: return int(json.loads(raw).get('percentage',0))
    except Exception: return 0
def gateway_id(): return 'gateway-'+str(uuid.getnode())[-6:]
