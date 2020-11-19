#!/usr/bin/env python3

from app import app, AUTH

user = AUTH.register_user(
    'test@test.com',
    'test'
)

reset_token = AUTH.get_reset_password_token(
    'test@test.com'
)

with app.test_client() as c:
    payload = {
        'email': "test@test.com",
        'reset_token': reset_token,
        'new_password': 'betty'
    }
    resp = c.put('/reset_password', data=payload)
    if resp.status_code != 200:
        print("Status code not 200")
        exit(0)
    if resp.get_json() != {
        'email': "test@test.com",
        'message': "Password updated"
    }:
        print('JSON return is not the same')
        exit(0)

    sessions_payload = {
        'email': 'test@test.com',
        'password': 'betty'
    }
    resp = c.post('/sessions', data=sessions_payload)
    if resp.status_code != 200:
        print("Wrong password for email")
        exit(0)

print("OK", end='')
