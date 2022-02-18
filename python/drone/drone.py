@DeprecationWarning
class Drone():

    __droneName = None
    __serialNumber = None

    __networkSSID = None
    __networkPass = None

    def __init__(self, droneName, serialNumber):
        self.__droneName = droneName
        self.__serialNumber = serialNumber;

    def setCredenticals(self, SSID, Pass):
        self.__networkSSID = SSID
        self.__networkPass = Pass

    def getCredenticals(self):
        return (self.__networkSSID, self.__networkPass)