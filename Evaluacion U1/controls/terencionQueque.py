from controls.dao.quequeDaoAdapter import QuequeDaoAdapter
from models.retencion import Retencion
class RetencionQueue(QuequeDaoAdapter):
    def __init__(self, useList: bool, size: int):
        super().__init__(Retencion, useList, size)
        self.__retencion = None
        
    @property
    def _retencion(self):
        if self.__retencion == None:
            self.__retencion = Retencion()
        return self.__retencion
    
    @_retencion.setter
    def _retencion(self, value):
        self.__retencion = value
        
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__retencion._id = self._lista._queque._class._length +1
        self._save(self.__retencion)
    
    
    
    
        