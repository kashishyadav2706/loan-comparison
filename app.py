from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


def calculate_emi(P, R, T):
    # If interest rate is 0
    if R == 0:
        emi = P / (T * 12)
        total_payment = P
        total_interest = 0
    else:
        R = R / (12 * 100)
        N = T * 12
        emi = (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)
        total_payment = emi * N
        total_interest = total_payment - P

    return {
        "emi": round(emi, 2),
        "total_interest": round(total_interest, 2),
        "total_payment": round(total_payment, 2)
    }


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    try:
        P = float(data.get("principal"))
        R = float(data.get("rate"))
        T = int(data.get("tenure"))

        if P <= 0 or R < 0 or T <= 0:
            return jsonify({"error": "Values must be greater than zero"}), 400

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing input fields"}), 400

    return jsonify(calculate_emi(P, R, T)), 200


@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "Backend is running 🚀"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
