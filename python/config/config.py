class Config:

    from io import FileIO as __FileIOException
    from json import loads as __json_serialize_function
    from json import dumps as __json_deserialize_function

    __config_file = None
    __data = None
    __jsonData = None

    def __init__(self, config_file):
        self.__config_file = config_file

    def getData(self):
        if self.__data == None:
            file = open(self.__config_file, 'r')
            self.__data = file.read()
            file.close()
        return self.__data

    def getJson(self):
        if self.__jsonData == None:
            self.__jsonData = self.__json_serialize_function(self.__data)
        return self.__jsonData

    def resetJson(self):
        self.__jsonData = None
        self.getJson()

    def saveJson(self):
        self.__data = self.__json_deserialize_function(self.__jsonData, indent=4)

    def saveData(self, force=False):
        if (self.__data != None) or force:
            file = open(self.__config_file, 'w')
            file.write(self.__data)
            file.close()
        else:
            raise self.__FileIOException('Veuillez renseigner des données à sauvegarder ou forcer la sauvegarde avec le paramètre force=True !')