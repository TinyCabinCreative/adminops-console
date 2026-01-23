NO PRIOR FLASK EXPERIENCE NEEDED

***************************************************************
USER NAME - admin
PASSWORD - admin123
***************************************************************
You should see the login page, and after logging in, the AdminOps dashboard.

1️⃣ Prerequisites

Make sure you have the following installed:

Python 3.10+
Check with:

python --version


Git
Check with:

git --version

2️⃣ Clone the Repository
git clone https://github.com/your-username/adminops-console.git
cd adminops-console

3️⃣ Create a Virtual Environment (Recommended)

This keeps dependencies isolated.
Please not if dependencies are already installed you can skip to #5 or #6 after starting the VENV.

Windows (PowerShell):
python -m venv venv
venv\Scripts\activate

macOS / Linux:
python3 -m venv venv
source venv/bin/activate


You should now see (venv) in your terminal.

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Set Flask Environment Variables
Windows (PowerShell):
$env:FLASK_APP="app:create_app"
$env:FLASK_ENV="development"

macOS / Linux:
export FLASK_APP=app:create_app
export FLASK_ENV=development

6️⃣ Initialize the Database

Start the Flask shell:

flask --app app:create_app shell


Then run:

from app.extensions import db
db.create_all()
exit()


This creates the SQLite database (adminops.db) and all tables.

7️⃣ Run the Application
flask --app app:create_app run


You should see output similar to:

Running on http://127.0.0.1:5000

8️⃣ Access the App

Open your browser and go to:

👉 http://127.0.0.1:5000

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