from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/")
def proxy():
    url = request.args.get("url")

    if not url:
        return "Add this to the end of the url (If it doesn't work go to cool-school-tech.onrender.com): ?url=https://your-website.com"

    r = requests.get(url)

    return Response(
        r.content,
        status=r.status_code,
        content_type=r.headers.get("Content-Type")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
