import sys
sys.dont_write_bytecode = True
import json

from flask            import jsonify
from flask            import Flask
from flask            import request
from flask_cors       import CORS

from entities import RESTLog
from entities import RMILog

from controller import CreateRESTLogController
from controller import CreateRMILogController

create_rest_log_controller = CreateRESTLogController()
create_rmi_log_controller  = CreateRMILogController()




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

@APP.route("/log/rest/new", methods = ["POST"])
def careate_rest_log():
    if (request.method == "POST"):
        
        request_parsed = request.get_json() 
        
        new_log = RESTLog(
            timestamp         = request_parsed["timestamp"],
            user_ip_address   = request_parsed["user_ip_address"],
            username          = request_parsed["username"],
            bytes_sent        = request_parsed["bytes_sent"],
            bytes_received    = request_parsed["bytes_received"],
            time_spent        = request_parsed["time_spent"],
            server_ip_address = request_parsed["server_ip_address"],
            server_port       = request_parsed["server_port"],
            http_method       = request_parsed["http_method"],
            url               = request_parsed["url"],                #uri-stem
            http_status       = request_parsed["http_status"],
        )

        response = create_rest_log_controller.handle(
            new_log
        )
        
        print(response)

        return json.dumps({
            "message": response, "status_code": 200
        }),200
                
@APP.route("/log/rmi/new", methods = ["POST"])
def careate_rmi_log():
    if (request.method == "POST"):
        
        request_parsed = request.get_json() 
        
        new_log = RMILog(
            timestamp         = request_parsed["timestamp"],
            user_ip_address   = request_parsed["user_ip_address"],
            username          = request_parsed["username"],
            bytes_sent        = request_parsed["bytes_sent"],
            bytes_received    = request_parsed["bytes_received"],
            time_spent        = request_parsed["time_spent"],
            server_ip_address = request_parsed["server_ip_address"],
            server_port       = request_parsed["server_port"],
            
            nameserver        = request_parsed["nameserver"],    
            object_name       = request_parsed["object_name"],
            object_method     = request_parsed["object_method"],
            response_status   = request_parsed["response_status"] 
        )

        response = create_rmi_log_controller.handle(
            new_log
        )
        
        print(response)

        return json.dumps({
            "message": response, "status_code": 200
        }),200


if (__name__ == "__main__"):
    print("> Starting log server at http://localhost:8080")
    APP.run(debug=True, port=8080)