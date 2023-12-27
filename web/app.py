from flask import Flask, render_template, request, jsonify

# import ngrok
from datetime import datetime

from database import Database
from alarm_table import AlarmTable

app = Flask(__name__)
db = Database()
alarm_table = AlarmTable()
db.init()
db.create_table(alarm_table)


@app.route("/")
def index():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", current_datetime=current_datetime)


@app.route("/alarm_page/")
def alarm_page():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alarms = db.get_table_in_rows(alarm_table)
    return render_template("alarm_page.html", current_datetime=current_datetime, alarms=alarms)


@app.route("/set_alarm/", methods=["POST"])
def set_alarm():
    data = request.get_json()
    print(data)
    print(type(data))
    alarm_table.add_alarm(data["time"], data["description"])
    db.insert(alarm_table)
    return {"status": "success"}


@app.route("/delete_alarm/", methods=["POST"])
def delete_alarm():
    data = request.get_json()
    print(data)
    db.delete(alarm_table.name, f"id={data['id']}")
    return {"status": "success"}


# def foreward_port(port: int):
#     listener = ngrok.forward(f"localhost:{port}", authtoken_from_env=True,
#                              oauth_provider="google")

#     print(f"Ingress established at: {listener.url()}")


if __name__ == "__main__":
    # foreward_port(5000)
    app.run(debug=True)
