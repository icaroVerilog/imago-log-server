import sys
sys.dont_write_bytecode = True
import json

from flask           import jsonify
from flask           import Flask
from flask           import request
from flask_cors      import CORS

from core.controller import CreateRESTLogController
from core.controller import RetrieveRESTLogController
from core.controller import CalculateAvgResponseTimeController

create_rest_log_controller             = CreateRESTLogController()
retrieve_rest_log_controller           = RetrieveRESTLogController()
calculate_avg_response_time_controller = CalculateAvgResponseTimeController()


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
    
@APP.errorhandler(405)
def route_not_found(error):
    code, message = str(error).split(": ")
    return json.dumps(
        {
            "message": message, 
            "status_code": 405
        }
    ), 405

# ================================ LOGS ROUTES ================================

@APP.route("/log/rest/new", methods = ["POST"])
def create_rest_log():
    if (request.method == "POST"):
        response = create_rest_log_controller.handle(request)
        return response

@APP.route("/log/rest/retrieve", methods = ["GET"])
def retrieve_rest_logs():
    if (request.method == "GET"):
        response = retrieve_rest_log_controller.handle(request)
        return response



@APP.route("/log/rest/metrics/avg-response-time", methods = ["GET"])
def average_response_time():
    if (request.method == "GET"):
        response = calculate_avg_response_time_controller.handle(request)
        return response


# @APP.route("/log/rmi/retrieve", methods = ["GET"])
# def retrieve_rmi_logs():
#     if (request.method == "GET"):
        
#         object_name     = request.headers["object-name"]
#         object_method   = request.headers["object-method"]
#         response_status = request.headers["response-status"]
#         server_ip       = request.headers["server-ip"]
#         date_day        = request.headers["date-day"]
#         date_month      = request.headers["date-month"]
#         date_year       = request.headers["date-year"]
        
#         parameters = RMILogRetrieveParameters(
#             object_name,
#             object_method,
#             response_status,
#             server_ip,
#             date_day,
#             date_month,
#             date_year,
#         )
        
#         response = retrieve_rmi_log_controller.handle(parameters)

#         return json.dumps({
#             "message": "success", "data": response , "status_code": 200
#         }),200

# @APP.route("/log/rmi/new", methods = ["POST"])
# def create_rmi_log():
#     if (request.method == "POST"):
        
#         request_parsed = request.get_json() 
        
#         new_log = RMILog(
#             timestamp         = request_parsed["timestamp"],
#             user_ip_address   = request_parsed["user_ip_address"],
#             username          = request_parsed["username"],
#             bytes_sent        = request_parsed["bytes_sent"],
#             bytes_received    = request_parsed["bytes_received"],
#             time_spent        = request_parsed["time_spent"],
#             server_ip_address = request_parsed["server_ip_address"],
#             server_port       = request_parsed["server_port"],
            
#             nameserver        = request_parsed["nameserver"],    
#             object_name       = request_parsed["object_name"],
#             object_method     = request_parsed["object_method"],
#             response_status   = request_parsed["response_status"] 
#         )

#         response = create_rmi_log_controller.handle(
#             new_log
#         )
        
#         print(response)

#         return json.dumps({
#             "message": response, "status_code": 200
#         }),200

if (__name__ == "__main__"):
    print("> Starting log server at http://localhost:8080")
    APP.run(debug=True, port=8083)
