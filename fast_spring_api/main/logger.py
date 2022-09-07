# logger

class FastSpringLogger:
    
    def info(self, msg: str):
        print(f'"INFO: {str(msg)}"')
    
    def error(self, msg: str):
        print(f'"ERROR: {str(msg)}"')
        
    def success(self, msg: str):
        print(f'"SUCCESS: {str(msg)}"')

