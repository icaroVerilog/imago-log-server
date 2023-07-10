import json

from flask         import Request
from core.services import CreateRESTLogService
from core.entities import RESTLog

class CreateRESTLogController:
    def handle(self, request:Request):
        create_rest_log_service = CreateRESTLogService()
        
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
        
        response = create_rest_log_service.execute(new_log)
        
        return json.dumps({
            "message": response, "status_code": 200
        }),200
        