import sys
sys.dont_write_bytecode = True
import json

from flask            import jsonify
from flask            import Flask
from flask            import request
from flask_cors       import CORS

from controller import CreateLogController

from entity import Log






create_log_controller = CreateLogController()




APP = Flask(__name__)

@APP.errorhandler(404)
def route_not_found(error):
    code, message = str(error).split(": ")
    return json.dumps(
        {
            "message": message, 
            "status_code": 404
        }
    ), 404

# ================================ USER ROUTES ================================

@APP.route("/log/new", methods = ["POST"])
def create_log():
    if (request.http_method == "POST"):
        
        request_parsed = request.get_json() 
        
        new_log = Log(
            timestamp         = request_parsed["timestamp"],
            user_ip_address   = request_parsed["user_ip_address"],
            username          = request_parsed["username"],
            http_method       = request_parsed["http_method"],
            url               = request_parsed["url"],                #uri-stem
            http_status       = request_parsed["http_status"],
            bytes_sent        = request_parsed["bytes_sent"],
            bytes_received    = request_parsed["bytes_received"],
            time_spent        = request_parsed["time_spent"],
            server_ip_address = request_parsed["server_ip_address"],
            server_port       = request_parsed["server_port"]
        )

        response = create_log_controller.handle(
            new_log
        )

        return response, 200
    else:
        return 400, 400
                



if (__name__ == "__main__"):
    print("> Starting log server at http://localhost:8080")
    APP.run(debug=True, port=8080)