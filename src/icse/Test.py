'''
Created on 22/mar/2012

@author: ximarx
'''
from icse.Queue import Queue
from random import Random

if __name__ == '__main__':
    
    q = Queue()
    for i in range(30):
        q.enqueue(Random().randint(1, 100))
    
    print "Contenuto della coda: ", q
    
    while q.isEmpty() == False:
        e = q.dequeue()
        print "Elemento eliminato dalla coda: ", e
        
    # la coda ora e' vuota, faccio tirare fuori l'eccezione
    try:
        q.dequeue()
    except Queue.EmptyError:
        print "Eccezione intercettata"
        print "La coda e' vuota? ", q.isEmpty()
    
    
    
    
    
