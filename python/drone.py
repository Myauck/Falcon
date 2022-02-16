class Drone:

    import dronekit as DroneAPI

    __host = '0.0.0.0'
    __port = 0

    __connection = None

    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    def connect(self):
        self.__connection = self.getAPI().connect(f'{self.host}:{self.port}', wait_ready=True)
    
    def disconnect(self):
        self.__connection = None

    def getConnection(self):
        return self.__connection

    def getAPI(self):
        return self.DroneAPI
    
