import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
  """ Return a friendly HTTP greeting. """
  return "<h1>Hello World!</h1>"

if __name__ == "__main__":
  app.run(host="localhost", port=8080, debug=True)
