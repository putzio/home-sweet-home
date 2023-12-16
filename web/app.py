from flask import Flask, render_template, request, jsonify

# import ngrok
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", current_datetime=current_datetime)


@app.route("/add_alarm")
def add_alarm():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alarms = [
        {"id": 1, "time": "2021-01-01 12:00:00", "description": "Wake up"},
        {"id": 2, "time": "2021-01-01 12:00:00", "description": "Take medicine"},
        {"id": 3, "time": "2021-01-01 12:00:00", "description": "Go to sleep"},
    ]
    return render_template("add_alarm.html", current_datetime=current_datetime, alarms=alarms)


@app.route("/api/set-color", methods=["POST"])
def set_color():
    data = request.get_json()
    # Process the RGB values (data['red'], data['green'], data['blue'])
    # Implement your logic to control the RGB lights here

    # For demonstration purposes, just echoing the received data
    return jsonify({"message": f'Color set to RGB({data["red"]}, {data["green"]}, {data["blue"]})'})


# def foreward_port(port: int):
#     listener = ngrok.forward(f"localhost:{port}", authtoken_from_env=True,
#                              oauth_provider="google")

#     print(f"Ingress established at: {listener.url()}")


if __name__ == "__main__":
    # foreward_port(5000)
    app.run(debug=True)
