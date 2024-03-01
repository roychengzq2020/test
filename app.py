from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    response = {
        "status": "up"
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)


