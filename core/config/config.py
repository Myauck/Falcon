class Config:

    from json import loads as __loads
    from json import dumps as __dumps

    __config_file: str = None
    __data = None
    __jsonData = None

    _instances: dict() = {}

    @staticmethod
    @classmethod
    def getInstance(name):
        if Config._instances[name] == None:
            raise Exception('Impossible de trouver l\'instance %s.' % name)
        return Config._instances[name]

    def __init__(self, config_name, config_file):
        self.__config_name = config_name
        self.__config_file = config_file
        self.__instances[self.__config_name] = self

    def getConfigFile(self) -> str:
        return self.__config_file
    
    def getConfigName(self) -> str:
        return self.__config_name

    def getData(self) -> list[str]:
        if self.__data == None:
            file = open(self.__config_file, 'r')
            self.__data = file.read();
            file.close()
        return self.__data

    def getJson(self) -> dict:
        if self.__jsonData == None:
            if self.__data == None:
                self.getData()
            self.__jsonData = self.__loads(self.__data)
        return self.__jsonData

    def resetJson(self) -> None:
        self.__jsonData = None
        self.getJson()

    def saveJson(self) -> None:
        self.__data = self.__dumps(self.__jsonData, sort_keys=True, indent=4)

    def saveData(self, force=False) -> None:
        if (self.__data != None) or force:
            file = open(self.__config_file, 'w')
            file.write(self.__data)
            file.close()
        else:
            raise Exception('Veuillez renseigner des données à sauvegarder ou forcer la sauvegarde avec le paramètre force=True !')
    
    pass