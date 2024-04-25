from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("../../data/predicted/combined_prediction.csv")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    # Use form data if JSON data is not found
    symbol = (
        request.form.get("symbol")
        if not request.is_json
        else request.json.get("symbol")
    )
    result = df[df["symbol"].str.upper() == symbol.upper()].drop_duplicates(
        subset="symbol", keep="last"
    )
    if not result.empty:
        return jsonify(
            {
                "symbol": symbol,
                "transcript_esg": result["transcript_esg"].iloc[-1],
                "predicted_esg_risk_level": result["predicted_esg_risk_level"].iloc[-1],
                "esg_score": result["esg_score"].iloc[-1],
            }
        )
    else:
        return jsonify({"error": "Symbol not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
