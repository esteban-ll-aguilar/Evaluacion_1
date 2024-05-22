from typing import TypeVar, Generic, Type
from controls.tda.queque.queque import Queque
import os, json
T = TypeVar("T")
class QuequeDaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T, useList: bool, size: int):
        self.atype = atype
        self.lista = Queque(size, useList)
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  + "/data/"
    
    def _list(self) -> T:
        if os.path.isfile(self.URL + self.file):
            f = open(self.URL + self.file, "r")
            datos = json.load(f)
            self.lista.clear
            for data in datos:
                a = self.atype().deserializar(data)
                self.lista.queque(a)
            f.close()
        return self.lista
    
    
    def __transform__(self):
        aux = '['
        for i in range(0, self.lista._queque._class._length):
            if i < self.lista._queque._class._length -1:
                #print(self.lista.get(i).serialize)
                aux += str(json.dumps(self.lista._queque._class.get(i).serialize)) + ','
            else:
                aux += str(json.dumps(self.lista._queque._class.get(i).serialize))
        aux += ']'
        return aux
    
    
    def to_dict(self):
        aux = []
        self._list()
        for i in range(0, self.lista._queque._class._length):
            aux.append(self.lista._queque._class.get(i).serialize)
        return aux
    

    def _save(self, data: T) -> T:
        self._list()
        
        self.lista.queque(data)
        f = open(self.URL + self.file, "w")
        print("Nombre del archivo: "+self.file)
        f.write(self.__transform__())
        f.close()