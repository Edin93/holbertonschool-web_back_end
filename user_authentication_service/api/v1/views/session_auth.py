#!/usr/bin/env python3
"""
auth module
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from flask import jsonify, make_response, request
from models.user import User
from os import getenv

from api.v1.views import app_views, abort


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ view for route /auth_session/login, method POST """
    u_email = request.form.get('email')
    if not u_email:
        return jsonify({"error": "email missing"}), 400
    u_password = request.form.get('password')
    if not u_password:
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': u_email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    for u in user:
        if u.is_valid_password(u_password):
            from api.v1.auth import auth
            session_id = auth.create_session(u.id)
            user_json = jsonify(u.to_json())
            user_json.set_cookie(getenv('SESSION_NAME'), session_id)
            return user_json
        else:
            return jsonify({"error": "wrong password"}), 401

@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """ view for route /auth_session/logout, method DELETE """
    from api.v1.auth import auth
    destroy_session_res = auth.destroy_session(request)
    if destroy_session_res is False:
        abort(404)
    else:
        return jsonify({}), 200
