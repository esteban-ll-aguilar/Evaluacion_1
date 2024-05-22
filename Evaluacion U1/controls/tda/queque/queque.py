from controls.tda.queque.quequeOperation import QuequeOperation
class Queque:
    def __init__(self, top, useList):
        self.__queque = QuequeOperation(top, useList)

    @property
    def _queque(self):
        return self.__queque

    @_queque.setter
    def _queque(self, value):
        self.__queque = value




    def queque(self, data):
        self.__queque.queque(data)
    
    @property
    def dequeque(self):
        return self.__queque.dequeque
    
    @property
    def print(self):
        self.__queque.print

    @property
    def verify(self):
        return self.__queque.verifyTop
    
    @property
    def clear(self):
        self.__queque._class.clear