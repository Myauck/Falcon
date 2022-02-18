
from glob import glob
import os
import log

class Logs():

    __logs: list[str] = None
    __json: dict = None
    __configInstance = None

    def __init__(self, path: str, log_config_instance):
        self.__configInstance = log_config_instance
        self.__logs = glob(os.path.join(path, '**', '*.log'))
        self.__json = self.__configInstance.getJson()
        pass

    def getFileList(self) -> list[str]:
        return self.__logs

    def getLogFile(self, file_id):
        file = self.__json['logfiles'][file_id]
        if file == '' or file == None:
            return None
        return LogFile(file)

    def getLastLogFile(self):
        lastFile = self.__json['variables']['lastfile']
        if lastFile == '' or lastFile == None:
            return None
        return LogFile(lastFile)

    def createNewLogFile(self):
        n = self.__json['variables']['n']
        n+=1
        self.__json['variables']['n'] = n
        return LogFile('%s.json' % n)

        