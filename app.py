from flask import Flask, jsonify
import os
app = Flask(__name__)
@app.route("/")
def home():
   return jsonify({
       "message": "Aplicação Python funcionando",
       "version": os.getenv("APP_VERSION", "local")
   })
@app.route("/health")
def health():
   return jsonify({"status": "ok"}), 200
@app.route("/error")
def error():
   return jsonify({"status": "error"}), 500
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)