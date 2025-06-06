from flask import Flask, request, render_template_string
import yaml
import requests

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "World")
    return render_template_string("Hello {{ " + name + " }}")

@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    r = requests.get(url, verify=False)
    return r.text

@app.route("/yaml", methods=["POST"])
def load_yaml():
    return yaml.load(request.data, Loader=yaml.Loader)

if __name__ == "__main__":
    app.run(debug=True)
