from flask import Flask, request, jsonify, render_template
import os  # Import os to read environment variables

app = Flask(__name__)

latest_data = {"message from pico": "No data yet"}  # Store the latest received data

@app.route("/")
def index():
    return render_template("index.html")  # Serve the webpage

@app.route("/data", methods=["POST"])
def receive_data():
    global latest_data
    data = request.get_json()
    print("Received Data:", data)  # Print received data in the terminal
    latest_data = data  # Store the latest received data
    return jsonify({"message": "Data received successfully!"})

@app.route("/latest-data")
def get_latest_data():
    return jsonify(latest_data)  # Send the latest received data to the webpage

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get port from Render, default to 5000 for local testing
    app.run(host="0.0.0.0", port=port, debug=True)  # Run on all network interfaces
