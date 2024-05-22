from controls.tda.linked.linkedList import Linked_List
from controls.tda.array.arrayList import ArrayList
from controls.exception.linkedListExeption import LinkedEmptyException
class QuequeOperation:
    def __init__(self, top, useList):
        self.__class = Linked_List() if useList else ArrayList()
        self.__top = top


    @property
    def _class(self):
        return self.__class

    @_class.setter
    def _class(self, value):
        self.__class = value


    @property
    def _top(self):
        return self.__top

    @_top.setter
    def _top(self, value):
        self.__top = value

    @property
    def verifyTop(self):
        return self._class._length < self.__top
    
    
    def queque(self, data):
        if self.verifyTop:
            self._class.add(data, self._class._length)
        else:
            raise LinkedEmptyException("Queque is Full")
        
    @property
    def dequeque(self):
        if self._class.isEmpty:
            raise LinkedEmptyException("Queque is Empty")
        else:
            self.detele(0)
            
    @property
    def print(self):
        for i in range(0, self._class._length):
            print(self._class.get(i))


    
