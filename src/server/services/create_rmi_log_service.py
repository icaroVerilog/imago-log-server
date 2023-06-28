import uuid

from database     import DatabaseConnection
from entities     import RMILog
from repositories import CreateLogRepository


class CreateRMILogService:
    def execute(self, log: RMILog):
        db_connection         = DatabaseConnection()
        create_log_repository = CreateLogRepository()    
        
        id = uuid.uuid4()
        
        response = create_log_repository.create_rmi_log(
            id,
            log,
            db_connection
        )
        
        return response
        
        