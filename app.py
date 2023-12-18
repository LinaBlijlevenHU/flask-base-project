# Importeer de belangrijke
from flask import Flask, render_template

app = Flask(__name__)


# Met app.route registreren we nieuwe pagina's in onze applicatie.
# Straks wil je meerdere routes en pagina's toe gaan voegen.
# Get started: https://www.turing.com/kb/build-flask-routes-in-python#what-is-a-route?
@app.route('/')
def index():
    # Render de HTML uit index.html.
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
