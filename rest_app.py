from flask import Flask, request, jsonify
from flask import Flask, request
from db_connector import DBConnector
import os
import signal
app = Flask(__name__)
db_connector = DBConnector()


@app.route('/users/<int:user_id>', methods=['POST'])
def create_user(user_id):
    try:
        user_name = request.json.get('user_name')
        if db_connector.user_exists(user_id):
            return jsonify({"status": "error", "reason": "id already exists"}), 500

        db_connector.add_user(user_id, user_name)
        return jsonify({"status": "ok", "user_added": user_name}), 200

    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user_name = db_connector.get_user(user_id)
        if user_name:
            return jsonify({"status": "ok", "user_name": user_name}), 200
        else:
            return jsonify({"status": "error", "reason": "no such id"}), 500

    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user_name = request.json.get('user_name')
        if db_connector.user_exists(user_id):
            db_connector.update_user(user_id, user_name)
            return jsonify({"status": "ok", "user_updated": user_name}), 200
        else:
            return jsonify({"status": "error", "reason": "no such id"}), 500

    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        if db_connector.user_exists(user_id):
            db_connector.delete_user(user_id)
            return jsonify({"status": "ok", "user_deleted": user_id}), 200
        else:
            return jsonify({"status": "error", "reason": "no such id"}), 500

    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500


@app.route('/stop_server', methods=['GET'])
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)