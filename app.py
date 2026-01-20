from flask import Flask, request, jsonify

app = Flask(__name__)

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
    data = request.json
    P = float(data["principal"])
    R = float(data["rate"])
    T = int(data["tenure"])

    return jsonify(calculate_emi(P, R, T))

if __name__ == "__main__":
    app.run()
