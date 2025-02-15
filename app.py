from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_data():
    data = request.json
    print(f"📩 Получены данные: {data}")
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
