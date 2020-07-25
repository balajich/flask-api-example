python -m venv env
env\Scripts\activate
pip install -r requirements.txt
set FLASK_APP=Server.py
flask run


# CURL
curl -i -v -H "Content-Type: application/json" -X POST -d "{\"message\":\"I hate  roads and windows curl utility\"}" http://localhost:5000/foo