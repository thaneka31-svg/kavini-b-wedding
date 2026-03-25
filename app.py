from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Temporary storage (later we will use database)
guest_response = {
    "adults": 0,
    "kids": 0,
    "elders": 0
}

event_date = datetime(2026, 8, 25, 18, 0, 0)

@app.route("/")
def home():
    now = datetime.now()
    diff = event_date - now
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60

    total = guest_response["adults"] + guest_response["kids"] + guest_response["elders"]

    return render_template(
        "home.html",
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        total=total
    )

@app.route("/rsvp", methods=["GET", "POST"])
def rsvp():
    if request.method == "POST":
        guest_response["adults"] = int(request.form.get("adults") or 0)
        guest_response["kids"] = int(request.form.get("kids") or 0)
        guest_response["elders"] = int(request.form.get("elders") or 0)
        return redirect(url_for("home"))

    return render_template("rsvp.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)