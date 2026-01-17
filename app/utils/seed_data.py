def seed_roles_permissions(db):
    from app.models import Role, Permission

    permissions = [
        "manage_users",
        "assign_roles",
        "view_systems",
        "edit_systems",
        "create_incidents",
        "resolve_incidents",
        "approve_changes",
        "view_audit_logs"
    ]

    perm_objects = {}
    for p in permissions:
        perm = Permission(name=p)
        db.session.add(perm)
        perm_objects[p] = perm

    super_admin = Role(name="SuperAdmin", permissions=list(perm_objects.values()))
    admin = Role(name="Admin", permissions=[
        perm_objects["manage_users"],
        perm_objects["view_systems"],
        perm_objects["edit_systems"],
        perm_objects["create_incidents"],
        perm_objects["view_audit_logs"]
    ])

    db.session.add_all([super_admin, admin])
    db.session.commit()
