from datetime import datetime

@DeprecationWarning
class Log():

    __log_file: str = None
    __commands: list(str) = None
    __startTime: datetime = None
    __endTime: datetime = None

    def __init__(self, log_file: str) -> None:
        super().__init__()
        self.__log_file = log_file
        self.__startTime = datetime.now()

    def getLogFile(self) -> str:
        return self.__log_file

    def getStartTime(self) -> datetime:
        return self.__startTime

    def getEndTime(self):
        if self.isFinished():
            return self.__endTime
        return -1

    def isFinished(self):
        return self.__endTime != None
    
    def getCommands(self):
        # À finir
        pass