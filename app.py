from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calculate_emi(P, R, T):
    R = R / (12 * 100)
    N = T * 12
    emi = (P * R * (1 + R)**N) / ((1 + R)**N - 1)
    total_payment = emi * N
    total_interest = total_payment - P

    return {
        "emi": round(emi, 2),
        "total_interest": round(total_interest, 2),
        "total_payment": round(total_payment, 2)
    }

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    try:
        P = float(data.get("principal"))
        R = float(data.get("rate"))
        T = int(data.get("tenure"))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing input fields"}), 400

    return jsonify(calculate_emi(P, R, T))

if __name__ == "__main__":
    app.run()
