import os
import firebase_admin
from firebase_admin import credentials, db

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyCELI3ddmszKAOL1_X2uuwz4A3mJxO4NFg",
    "authDomain": "slayer-bot-pro-v2.firebaseapp.com",
    "databaseURL": "https://slayer-bot-pro-v2-default-rtdb.firebaseio.com",
    "projectId": "slayer-bot-pro-v2",
    "storageBucket": "slayer-bot-pro-v2.appspot.com",
    "messagingSenderId": "432320404402",
    "appId": "1:432320404402:web:63bda5bf449d732a22a2ab",
    "measurementId": "G-9RT2B4YGC4",
}

_initialized = False

def initialize_firebase():
    global _initialized
    if _initialized:
        return
    if not firebase_admin._apps:
        service_account = os.getenv("FIREBASE_SERVICE_ACCOUNT")
        if service_account and os.path.exists(service_account):
            cred = credentials.Certificate(service_account)
            firebase_admin.initialize_app(cred, {"databaseURL": FIREBASE_CONFIG["databaseURL"]})
        else:
            firebase_admin.initialize_app(options={"databaseURL": FIREBASE_CONFIG["databaseURL"]})
    _initialized = True

def ref(path: str):
    initialize_firebase()
    return db.reference(path)
