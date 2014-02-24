from functools import wraps
from flask import request, redirect, url_for, session, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'username' in session :
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
