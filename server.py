from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "vivek is running", 200  # Simple message to confirm it's working

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        print("Received data:", data)
        return jsonify({"message": "Data received successfully!"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
