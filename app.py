from flask import Flask

#create a Flask application instance
app = Flask(__name__)

#added app routes
@app.route('/')
def index():
    return "<p>Hello World</p>"

#configure how the app is  run
if __name__ == "__main__":
    app.run(port=5000, debug=True)