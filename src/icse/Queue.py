'''
Created on 22/mar/2012

@author: ximarx
'''

class Queue:
    '''
    Struttura dati coda
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__list = []
        
    def enqueue(self, elem):
        '''
        Inserisce un nuovo elemento in coda
        '''
        self.__list.append(elem)
        
    def dequeue(self):
        '''
        Rimuove e ritorna il primo elemento della coda
        '''
        if ( self.isEmpty() != True ):
            return self.__list.pop(0)
        else:
            raise Queue.EmptyError("La coda e' vuota")
        
    def isEmpty(self):
        '''
        Controlla se la coda e' vuota
        '''
        return (len( self.__list ) == 0)
        
    def __len__(self):
        '''
        Ritorna la lunghezza della coda
        '''
        return len(self.__list) 
        
    def __str__(self):
        '''
        Stampa il contenuto della coda
        '''
        return repr(self.__list)
        
    class EmptyError(Exception):
        '''
        Eccezione che indica dequeue da coda vuota
        '''
        def __init__(self, value):
            self.value = value
            
        def __str__(self):
            return repr(self.value)
    