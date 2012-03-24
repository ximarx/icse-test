'''
Created on 24/mar/2012

@author: ximarx
'''
from icse.BinTree import BinTree

class SearchTree:
    '''
    Implementazione di albero di ricerca binaria
    '''

    def __init__(self, elements = []):
        '''
        Constructor
        '''
        self.__tree = BinTree(None)
        if ( len(elements) > 0 ):
            for el in elements :
                self.insert(el)
        
    def insert(self, element):
        '''
        Inserisce un elemento in un albero di ricerca
        '''
        root = self.__tree
        # semplicemente aggiungo come root element
        if root.get_value() == None :
            root.set_value(element)
            return True
        else:
            return self.__insert(element, root)
            
        
    def __insert(self, element, node):
        '''
        Implementazione ricorsiva inserimento elemento.
        L'elemento viene eseguito seguendo queste modalita':
            - se il nodo ha valore superiore, cerco nel ramo sinistro
            - se il nodo ha valore inferiore, cerco nel nodo destro
            - inserisco come nuovo nodo se il nodo nn ha figlio (sx o dx)
        '''
        node_val = node.get_value()
        if node_val > element:
            if node.has_left() == True :
                return self.__insert(element, node.get_left())
            else:
                node.set_left(element)
            return True
        elif node_val < element:
            if node.has_right() == True :
                return self.__insert(element, node.get_right())
            else:
                node.set_right(element)
            return True
        else:
            # node == element
            # ignoro il doppio inserimento
            return False
            
        
    def is_in(self, element):
        '''
        Controlla se l'elemento esiste nell'albero di ricerca
        '''
        node = self.__tree
        
        try:
            '''
            Continua ad andare in profondita'
            fino a trovare un elemento elemento
            o fino a quando non ci sono piu
            nodi da visitare
            '''
            while True:
                val = node.get_value()
                if val == element:
                    return True
                elif val > element:
                    node = node.get_left()
                elif val < element:
                    node = node.get_right()
        
        except BinTree.ChildMissingError:
            return False 
    
    def __str__(self):
        return str(self.__tree)
        
        