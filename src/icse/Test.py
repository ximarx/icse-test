'''
Created on 22/mar/2012

@author: ximarx
'''
from icse.Queue import Queue
from random import Random
from icse.BinTree import BinTree, BinTree_prettyPrint

if __name__ == '__main__':
    
    q = Queue()
    for i in range(30):
        q.enqueue(Random().randint(1, 100))
    
    print "Contenuto della coda: ", q
    
    print "Lunghezza coda: " , len(q)
    
    while q.isEmpty() == False:
        e = q.dequeue()
        print "Elemento eliminato dalla coda: ", e
        
    # la coda ora e' vuota, faccio tirare fuori l'eccezione
    try:
        q.dequeue()
    except Queue.EmptyError:
        print "Eccezione intercettata"
        print "La coda e' vuota? ", q.isEmpty()
    
    
    b = BinTree(1, None, BinTree(2), BinTree(3) )
    
    b.get_left().set_left(4)
    b.get_left().set_right(5)
    
    print b
    
    print BinTree_prettyPrint(b)
    
    
