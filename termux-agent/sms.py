import subprocess

def send_sms(number, message):
    try:
        subprocess.check_call(['termux-sms-send','-n',number,message])
        return True, None
    except Exception as exc:
        return False, str(exc)
