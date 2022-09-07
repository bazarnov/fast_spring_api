# logger

class FastSpringLogger:
    
    def info(self, msg: str) -> str:
        print(f'"INFO: {str(msg)}"')
    
    def error(self, msg: str) -> str:
        print(f'"ERROR: {str(msg)}"')
        
    def success(self, msg: str) -> str:
        print(f'"SUCCESS: {str(msg)}"')
        
    def fatal(self, msg: str) -> str:
        print(f'"FATAL: {str(msg)}"')

