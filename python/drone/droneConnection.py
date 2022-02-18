from config.configurable import Configurable
from config.config import Config as ConfigClass
import drone as DroneClass

@DeprecationWarning
class DroneConnection(Configurable):

    CONFIG_SECTION: str = "connection"
    __config: ConfigClass = None
    __drone: DroneClass = None

    def __init__(self, config: ConfigClass, drone: DroneClass):
        super().__init__()
        self.__config = config[self.CONFIG_SECTION]
        self.__drone = drone

    def getConfig(self) -> dict:
        super().getConfig()
        return self.__config

    def getConfigSection(self) -> str:
        super().getConfigSection()
        return self.CONFIG_SECTION

    def getDrone(self):
        return self.__drone

    def connect(self):
        #Apply Socket
        pass
