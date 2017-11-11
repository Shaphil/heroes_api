from flask import Flask

app = Flask(__name__)

import heroes_api.views
