from core.database import DatabaseConnection
from core.entities import RESTLogMetricParameters
from core.repositories import RetrieveLogRepository

class CalculateAvgResponseTimeService:
    def average(logs):
        pass
    
    def execute(self, parameters:RESTLogMetricParameters):
        db_connection           = DatabaseConnection()
        retrieve_log_repository = RetrieveLogRepository()    
        
        response = retrieve_log_repository.retrieve_rest_log(
            parameters,
            db_connection
        )
        
        sum = 0
        counter = 0
        
        for log in response:
            counter = counter + 1
            sum = sum + log[6]
        
        response = sum/counter
        return response