from heroes_api import app


@app.route('/')
def index():
    return 'Hello'
