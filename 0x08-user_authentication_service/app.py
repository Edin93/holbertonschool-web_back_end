#!/usr/bin/env python3
from flask import Flask, jsonify, request, make_response, abort, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def get_home():
    """ Returns home page result. """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ Returns a user if exists. """
    try:
        password = request.form['password']
        email = request.form['email']
        user = AUTH.register_user(email, password)
        if user:
            return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    User login function.
    """
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        msg = jsonify({"email": email, "message": "logged in"})
        res = make_response(msg)
        res.set_cookie('session_id', session_id)
        return res
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    User logout function.
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    else:
        AUTH.destroy_session(user.id)
        return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """
    Get existing user email.
    """
    sessiond_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
