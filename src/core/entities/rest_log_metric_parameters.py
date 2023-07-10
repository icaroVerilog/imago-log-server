class RESTLogMetricParameters:
    def __init__(
        self,
        http_method,
        url,
        start_date_day,
        start_date_month,
        start_date_year,
        end_date_day,
        end_date_month,
        end_date_year
    ):
        
        self.http_method      = None if http_method      == "None" else http_method
        self.url              = None if url              == "None" else url
        self.start_date_day   = None if start_date_day   == "None" else start_date_day
        self.start_date_month = None if start_date_month == "None" else start_date_month
        self.start_date_year  = None if start_date_year  == "None" else start_date_year
        self.end_date_day     = None if end_date_day     == "None" else end_date_day
        self.end_date_month   = None if end_date_month   == "None" else end_date_month
        self.end_date_year    = None if end_date_year    == "None" else end_date_year
        