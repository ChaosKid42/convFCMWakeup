#!/usr/bin/env python

from pyfcm import FCMNotification
import sys
import sqlite3

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
API_KEY = "secret"

c = sqlite3.connect('/var/lib/p2/TargetStore.db')
push_service = FCMNotification(api_key = API_KEY)


for row in c.execute('SELECT * FROM target'):
    device, domain, token, node, secret = row
    print(row)
    result = push_service.notify_single_device(registration_id=token, data_message={"account": device}, collapse_key=device[:6], delay_while_idle=False)
    print(result)
