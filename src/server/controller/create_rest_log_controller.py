from services import CreateRESTLogService
from entities import RESTLog



class CreateRESTLogController:
    def handle(self, log:RESTLog):
        create_log_service = CreateRESTLogService()
        response = create_log_service.execute(log)
        
        return response