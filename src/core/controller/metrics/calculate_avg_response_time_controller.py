import json

from flask         import Request
from core.services import CalculateAvgResponseTimeService
from core.entities import RESTLogRetrieveParameters

class CalculateAvgResponseTimeController:
    def handle(self, request:Request):
        calculate_avg_response_time_service = CalculateAvgResponseTimeService()
        
        parameters = RESTLogRetrieveParameters(
            http_method = request.headers["http-method"],
            http_status = request.headers["http-status"],
            url         = request.headers["url"],
            server_ip   = request.headers["server-ip"],
            date_day    = request.headers["date-day"],
            date_month  = request.headers["date-month"],
            date_year   = request.headers["date-year"]
        )
        
        response = calculate_avg_response_time_service.execute(parameters)
        
        
        return json.dumps({
            "message": "success", "data": response , "status_code": 200
        }), 200