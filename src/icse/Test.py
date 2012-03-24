'''
Created on 22/mar/2012

@author: ximarx
'''
from icse.Queue import Queue
from random import Random
from icse.BinTree import BinTree, BinTree_prettyPrint
from icse.SearchTree import SearchTree
import sys

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
    
    
    search = SearchTree([40,20,11,17,5,32])
    
    print "Elemento gia presente reinserito? ", search.insert(20)
    
    for val in [50,45,32,80]:
        if search.insert(val) == False :
            print >> sys.stderr,  "Elemento ignorato perche gia' esistente: " + str(val) 
    
    print search
    
