CREATE_REST_LOG = '''
    INSERT INTO 
        log_rest (
            id, 
            timestamp, 
            user_ip_address,
            username, 
            bytes_sent,
            bytes_received, 
            time_spent,
            server_ip_address, 
            server_port,
            http_method, 
            url, 
            http_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

CREATE_RMI_LOG = '''
    INSERT INTO 
        log_rmi (
            id, 
            timestamp, 
            user_ip_address,
            username, 
            bytes_sent,
            bytes_received, 
            time_spent,
            server_ip_address, 
            server_port,
            nameserver,
            object_name,
            object_method,
            response_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''