from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Load Firebase credentials (Download your service account JSON from Firebase Console)
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://dustbinmonitor-c5e71-default-rtdb.firebaseio.com/"
})

@app.route("/")
def index():
    return render_template("index.html")  # Your webpage

@app.route("/get-data")
def get_data():
    ref = db.reference("data")  # Change to match your Firebase path
    data = ref.get()
    return jsonify(data)  # Return Firebase data as JSON

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
