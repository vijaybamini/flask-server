from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Store received data (initially empty)
latest_data = {"message": "No data received yet"}

# Route to receive data from Pico W
@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    latest_data = request.get_json()  # Store received JSON data
    print("Received data:", latest_data)
    return jsonify({"message": "Data received successfully!"})

# Route to serve the webpage
@app.route('/')
def index():
    return render_template('index.html')  # Load the webpage

# Route to send the latest data to the webpage
@app.route('/latest-data')
def get_latest_data():
    return jsonify(latest_data)  # Send stored data as JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Accessible from mobile
