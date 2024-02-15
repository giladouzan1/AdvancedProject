# from flask import jsonify
# from flask import Flask, request
# from db_connector import DBConnector
# import os
# import signal
# app = Flask(__name__)
# db_connector = DBConnector()
#
#
# @app.route('/users/<int:user_id>', methods=['POST'])
# def create_user(user_id):
#     try:
#         user_name = request.json.get('user_name')
#         if db_connector.get_user(user_id):
#             return jsonify({"status": "error", "reason": "id already exists"}), 500
#
#         db_connector.add_user(user_id, user_name)
#         return jsonify({'status': 'ok', 'user_name': user_name}), 200
#
#     except Exception as e:
#         return jsonify({"status": "error", "reason": str(e)}), 500
#
#
# @app.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     try:
#         user_name = db_connector.get_user(user_id)
#         if user_name:
#             return {'status': 'ok', 'user_name': user_name}, 200
#         else:
#             return jsonify({"status": "error", "reason": "no such id"}), 500
#
#     except Exception as e:
#         return jsonify({"status": "error", "reason": str(e)}), 500
#
#
# @app.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     try:
#         user_name = request.json.get('user_name')
#         if db_connector.get_user(user_id):
#             db_connector.update_user(user_id, user_name)
#             return {'status': 'ok', 'user_name': user_name}, 200
#         else:
#             return jsonify({"status": "error", "reason": "no such id"}), 500
#
#     except Exception as e:
#         return jsonify({"status": "error", "reason": str(e)}), 500
#
#
# @app.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     try:
#         if db_connector.get_user(user_id):
#             db_connector.delete_user(user_id)
#             return {'status': 'ok', 'Deleted_user_id': user_id}, 200
#         else:
#             return jsonify({"status": "error", "reason": "no such id"}), 500
#
#     except Exception as e:
#         return jsonify({"status": "error", "reason": str(e)}), 500
#
#
# @app.route('/stop_server', methods=['GET'])
# def stop_server():
#     os.kill(os.getpid(), signal.SIGINT)
#     return 'Server stopped'
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3000)
from flask import Flask, request
from db_connector import DBConnector
import os
import signal

app = Flask(__name__)
mdb_connector = DBConnector()


@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        mdb_connector.add_user(user_id, user_name)
        return {'status': 'ok', 'user name': user_name}, 200  # status code
    elif request.method == 'GET':
        user_name = mdb_connector.get_user(user_id)
        return {'status': 'ok', 'user_name': user_name}, 200
    elif request.method == 'PUT':
        request_data = request.json
        new_name = request_data.get('user_name')
        mdb_connector.update_user(user_id, new_name)
        return {'status': 'ok', 'new_username': new_name}, 200
    elif request.method == 'DELETE':
        mdb_connector.delete_user(user_id)
        return {'Deleted user_id': user_id}, 200


@app.route('/stop_server', methods=['GET'])
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server stopped'


if __name__ == '__main__':
    # need to change host for other jenkinsfile
    app.run(host='0.0.0.0', port=3000)
