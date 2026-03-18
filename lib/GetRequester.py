import os
from flask import Flask, render_template
import requests

# Determine project root and templates folder
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
templates_path = os.path.join(project_root, "templates")

# Initialize Flask with the correct template folder
app = Flask(__name__, template_folder=templates_path)


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Raise error if request fails
        return response

    def load_json(self):
        return self.get_response_body().json()


@app.route('/')
def index():
    # JSON endpoint
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)
    people = requester.load_json()  # Fetches latest JSON
    return render_template("index.html", people=people)


if __name__ == '__main__':
    # Run Flask app from project root
    app.run(debug=True)