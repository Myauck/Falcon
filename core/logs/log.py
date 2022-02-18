from io import SEEK_END, SEEK_SET, TextIOWrapper

class LogFile():

    __fileName: str = None
    __fileRessource: TextIOWrapper = None

    def __init__(self, file) -> None:
        self.__fileName = file
        self.__fileRessource = open(file=self.__file, mode='ta+', encoding='utf-8')
        pass

    def getFileName(self) -> str:
        return self.__config_file

    def read(self):
        self.__fileRessource.seek(0, SEEK_SET)
        content = self.__fileRessource.readlines()
        self.__fileRessource.seek(0, SEEK_END)
        return content

    def writeAll(self, content, end=False):
        if end:
            self.append(content)
        else:
            self.__fileRessource.seek(0, SEEK_SET)
            self.__fileRessource.writelines(content)

    def append(self, new_content):
        self.__fileRessource.seek(0, SEEK_END)
        self.__fileRessource.writelines(new_content)
        pass

    def __del__(self):
        if not self.__fileRessource.closed():

            self.__fileRessource.close()
        global debug
        if debug:
            print('Ficher log %s s\'est correctement fermé' % self.__fileName)

    pass