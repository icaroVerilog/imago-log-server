import uuid

from database     import DatabaseConnection
from entities     import RESTLog
from repositories import CreateLogRepository


class CreateRESTLogService:
    def execute(self, log: RESTLog):
        db_connection         = DatabaseConnection()
        create_log_repository = CreateLogRepository()    
        
        id = uuid.uuid4()
        
        response = create_log_repository.create_rest_log(
            id,
            log,
            db_connection
        )
        
        return response
        
        