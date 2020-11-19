#!/usr/bin/env python3
"""
Module to assert the API routes proper behavior
"""
import requests
import json


URL = 'http://0.0.0.0:5000'


def register_user(email: str, password: str) -> None:
    """ Asserts this function's corresponding API route. """
    data = {'email': email, 'password': password}
    r = requests.post(URL + '/users', data=data)
    assert r.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """ Asserts this function's corresponding API route. """
    data = {'email': email, 'password': password}
    r = requests.post(URL + '/sessions', data=data)
    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    """ Asserts this function's corresponding API route. """
    data = {'email': email, 'password': password}
    r = requests.post(URL + '/sessions', data=data)
    assert r.status_code == 200
    return r.cookies.get('session_id')


def profile_unlogged() -> None:
    """ Asserts this function's corresponding API route. """
    r = requests.get(URL + '/profile')
    assert r.status_code == 403


def profile_logged(session_id: str) -> None:
    """ Asserts this function's corresponding API route. """
    user_session = log_in(EMAIL, PASSWD)
    cookies = {
        'session_id': user_session
    }
    r = requests.get(URL + '/profile', cookies=cookies)
    assert r.status_code == 200


def log_out(session_id: str) -> None:
    """ Asserts this function's corresponding API route. """
    user_session = log_in(EMAIL, PASSWD)
    cookies = {
        'session_id': user_session
    }
    r = requests.delete(URL + '/sessions', cookies=cookies)
    assert r.status_code == 200


def reset_password_token(email: str) -> str:
    """ Asserts this function's corresponding API route. """
    data = {
        'email': email
    }
    r = requests.post(URL + '/reset_password', data=data)
    assert r.status_code == 200
    data = json.loads(r.content)
    return data.get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Asserts this function's corresponding API route. """
    data = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    }
    r = requests.put(URL + '/reset_password', data=data)
    assert r.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
