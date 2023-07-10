import json

from flask         import Request
from core.services import RetrieveRESTLogService
from core.entities import RESTLogRetrieveParameters

class RetrieveRESTLogController:
    def __init__(self):
        self.response_ids = (
            "id", 
            "timestamp", 
            "user_ip_address",
            "username", 
            "bytes_sent",
            "bytes_received", 
            "time_spent",
            "server_ip_address", 
            "server_port",
            "http_method",
            "url",
            "http_status"
        )
    def handle(self, request:Request):
        retrieve_rest_log_service = RetrieveRESTLogService()
        
        parameters = RESTLogRetrieveParameters(
            http_method = request.headers["http-method"],
            http_status = request.headers["http-status"],
            url         = request.headers["url"],
            server_ip   = request.headers["server-ip"],
            date_day    = request.headers["date-day"],
            date_month  = request.headers["date-month"],
            date_year   = request.headers["date-year"]
        )
        
        response = retrieve_rest_log_service.execute(parameters)
        
        formated_response = []
        
        for log in response:
            formated_response.append(dict(zip(self.response_ids, log)))        
        
        return json.dumps({
            "message": "success", "data": formated_response , "status_code": 200
        }), 200