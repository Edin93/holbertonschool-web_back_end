#!/usr/bin/env python3
""" Contains SessionAuth routes handling.
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login() -> str:
    """ POST /api/v1/auth_session/login
    """
    email = request.form.get('email', None)
    if email is None or not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password', None)
    if password is None or not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]
    valid_pw = user.is_valid_password(password)
    if not valid_pw:
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    sessionId = auth.create_session(user.id)
    cookie_name = getenv('SESSION_NAME')
    result = jsonify(user.to_json())
    result.set_cookie(cookie_name, sessionId)
    return result


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_auth_logout() -> str:
    """ DELETE /auth_session/logout
    """
    from api.v1.app import auth

    if auth.destroy_session(request) is False:
        abort(404)

    return jsonify({}), 200
