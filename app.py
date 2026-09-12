from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Video Generator Backend is Running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    return jsonify({
        "status": "success",
        "message": "AI video generation request received",
        "prompt": prompt
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
