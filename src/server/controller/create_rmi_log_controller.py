from services import CreateRMILogService
from entities import RMILog



class CreateRMILogController:
    def handle(self, log:RMILog):
        create_log_service = CreateRMILogService()
        response = create_log_service.execute(log)
        
        return response