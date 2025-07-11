log_levels = {
    "info":"INFO",
    "error":"ERROR"
}

class ThirdPartyLogger:
    def write_log(self, message:str, severity:str):
        print(f"[{severity.upper()}] {message}")
        
class Logger:
    def info(self, message:str):
        pass

    def error(self, message:str):
        pass
    
class LoggerAdapter(Logger):
    def __init__(self, third_party:ThirdPartyLogger):
        self.third_party = third_party
        
    def info(self, message:str):
        self.third_party.write_log(message, log_levels["info"])
    
    def error(self, message):
        self.third_party.write_log(message, log_levels["error"])
        
logger = LoggerAdapter(ThirdPartyLogger())
logger.info("Service started")
logger.error("Something went wrong")