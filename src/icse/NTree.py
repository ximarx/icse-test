'''
Created on 24/mar/2012

@author: ximarx
'''

class NTree:
    '''
    Implementazione di albero N-ario con liste di figli
    '''


    def __init__(self, value = None, childs = []):
        '''
        Constructor
        '''
        self.__childs = []
        if isinstance(childs, [].__class__) :
            for i in childs :
                self.append_child(i)
        self.__parent = None
        self.__value = value
        
    def is_root(self):
        '''
        Controlla se il nodo e' radice
        '''
        return (self.__parent == None)
    
    def set_parent(self, parent):
        if isinstance(parent, NTree) == False :
            parent = NTree(parent)
        self.__parent = parent
    
    def get_parent(self):
        if self.is_root() == False:
            return self.__parent
        else:
            raise NTree.OrphanNodeError("Il nodo e' radice")
    
    def set_value(self, value):
        '''
        Imposta il valore del nodo
        '''
        self.__value = value
        
    def get_value(self):
        '''
        Restituisce il valore del nodo
        '''
        return self.__value
    
    def __adopt_child(self, value):
        if isinstance(value, NTree) == False :
            value = NTree(value)
            
        value.set_parent(self)
        return value
    
    def append_child(self, value):
        '''
        Inserisce un nuovo figlio come ultimo
        '''
        value = self.__adopt_child(value)
        self.__childs.append(value)
            
        
    def insert_child(self, value, index):
        '''
        Inserisce un nuovo figlio ad una posizione determinata
        '''
        value = self.__adopt_child(value)
        self.__childs.insert(index, value)
        
    def get_child(self, index):
        '''
        Restituisce il NODO figlio ad una determinata posizione
        '''
        if index < 0 or index >= len(self.__childs):
            raise NTree.InvalidChildIndexError("Indice figlio non valido")
        else:
            return self.__childs[index]
        
    def get_firstchild(self):
        '''
        Restituisce il primo NODO figlio
        '''
        return self.get_child(0)
    
    def get_childs(self):
        '''
        Restituisce la lista di nodi figli
        '''
        return self.__childs
        
    def get_childscount(self):
        '''
        Restituisce il numero di figli
        '''
        return len(self.__childs)
    
    def __str__(self):
        s = repr(self.__value)
        for i in self.__childs :
            s += " ( " + str(i) + " ) "
        return s
    
    class NTreeError(Exception):
        '''
        Eccezione che indica hasChild con tipo non valido
        '''
        def __init__(self, value):
            self.value = value
            
        def __str__(self):
            return repr(self.value)

    
    class OrphanNodeError(NTreeError):
        '''
        Indica che il nodo non ha padre
        '''
        def __init__(self, value):
            NTree.NTreeError.__init__(self, value)


    class InvalidChildIndexError(NTreeError):
        '''
        Indice del figlio richiesto mancante
        '''
        def __init__(self, value):
            NTree.NTreeError.__init__( self, value)

    
    