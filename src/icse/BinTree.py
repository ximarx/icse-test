'''
Created on 23/mar/2012

@author: ximarx
'''

class BinTree:
    '''
    Implementazione di albero binario
    '''

    CHILD_LEFT = 0
    CHILD_RIGHT = 1

    def __init__(self, value, parent = None, sx = None, dx = None):
        '''
        Constructor
        '''
        self.value = value
        if parent != None :
            self.set_child_of(parent)
        else:
            self.__parent = None
        if sx != None :
            self.set_left(sx)
        else:
            self.__sx = None
        if dx != None :
            self.set_right(dx)
        else:
            self.__dx = None
        
    def is_root(self):
        return (self.__parent == None)
    
    def has_child(self, childType):
        if childType == BinTree.CHILD_LEFT :
            return (self.__sx != None)
        elif childType == BinTree.CHILD_RIGHT :
            return (self.__dx != None)
        else:
            raise BinTree.ChildTypeError("Tipo di figlio non valido")
        
    def has_left(self):
        return self.has_child(BinTree.CHILD_LEFT)

    def has_right(self):
        return self.has_child(BinTree.CHILD_RIGHT)

    def is_leaf(self):
        return ( self.has_left() == False and self.has_right() == False )

    def get_left(self):
        if self.has_left():
            return self.__sx
        else:
            raise BinTree.ChildMissingError("Il nodo non ha figlio sinistro")

    def get_right(self):
        if self.has_right():
            return self.__dx
        else:
            raise BinTree.ChildMissingError("Il nodo non ha figlio destro")
    
    def get_value(self):
        return self.value

    def get_parent(self):
        return self.__parent
    
    def set_child_of(self, parent):
        if isinstance(parent, BinTree) == True :
            self.__parent = parent
        else: 
            raise TypeError("Il padre deve essere di tipo BinTree")
        
    def set_left(self, sx):
        if isinstance(sx, BinTree) == False :
            sx = BinTree(sx)
        sx.set_child_of(self)
        self.__sx = sx
        
    def set_right(self, dx):
        if isinstance(dx, BinTree) == False :
            dx = BinTree(dx)
        dx.set_child_of(self)
        self.__dx = dx
        
    def __str__(self):
        return repr(self.value) + " ( " + str(self.__sx) + " ) ( " + str(self.__dx) + " )"

    class BinTreeError(Exception):
        '''
        Eccezione che indica hasChild con tipo non valido
        '''
        def __init__(self, value):
            self.value = value
            
        def __str__(self):
            return repr(self.value)

    
    class ChildTypeError(BinTreeError):
        '''
        Eccezione che indica hasChild con tipo non valido
        '''
        def __init__(self, value):
            super.__init__(self, value)


    class ChildMissingError(BinTreeError):
        '''
        Eccezione che indica la mancanza di un figlio
        '''
        def __init__(self, value):
            super.__init__(self, value)


def BinTree_prettyPrint(root):
    
    b = ""
    
    if root.has_left() == True:
        b = b + "(" + BinTree_prettyPrint(root.get_left()) + ")"
    else:
        b = b + "()"
    
    b = b + " [" + str(root.get_value()) + "] "
    
    if root.has_right() == True:
        b = b + "(" + BinTree_prettyPrint(root.get_right()) + ")"
    else:
        b = b + "()"

    return b