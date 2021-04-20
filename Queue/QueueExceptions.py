class QueueEmptyException(RuntimeError): 
    def __init__(self, arg): 
        self.arg = arg 

class QueueFullException(RuntimeError): 
    def __init__(self, arg): 
        self.arg = arg 