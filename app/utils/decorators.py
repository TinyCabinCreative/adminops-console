from flask_login import current_user
from flask import abort
from functools import wraps

def require_permission(permission_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)

            if not current_user.role:
                return func(*args, **kwargs)

            permissions = [p.name for p in current_user.role.permissions]
            if permission_name not in permissions:
                abort(403)

            return func(*args, **kwargs)
        return wrapper
    return decorator
