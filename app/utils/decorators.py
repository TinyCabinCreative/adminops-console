from flask_login import current_user
from flask import abort

def require_permission(permission_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)

            permissions = [p.name for p in current_user.role.permissions]
            if permission_name not in permissions:
                abort(403)

            return func(*args, **kwargs)
        return wrapper
    return decorator
