NO PRIOR FLASK INSTRUCTIONS NEEDED

***************************************************************
USER NAME - admin
PASSWORD - admin123
***************************************************************
You should see the login page, and after logging in, the AdminOps dashboard.

🛠 Helpful Notes

Static assets (CSS) are served from app/static/

Templates live in app/templates/

Routes are organized by feature using Flask Blueprints

This app is intended for local development and learning, not production

🧠 Common Troubleshooting

Database errors?
Delete adminops.db and rerun Step 6.

Route not found?
Make sure the blueprint name and url_for() endpoint match.

Permission errors?
Ensure the logged-in user has a role assigned.