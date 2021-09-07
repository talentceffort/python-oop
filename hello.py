# source venv/bin/activate

# pip freeze > requirement.txt
from flask import Flask

app = Flask(__name__)

print(app)
