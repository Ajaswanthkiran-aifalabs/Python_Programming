
from collections import deque


class Queue:

    def __init__(self,maxlen=10):


        self.queue=[]
        self.waiting=[]
        self.maxlen=maxlen

    def _add_job(func):

        def inner_fun(self,value):
            if len(self.queue)==self.maxlen:
                print()
                print("Currently all jobs are filled")
                self.waiting.append(value)
                print("The element in the waiting list :",self.waiting)
            else:
                func(self,value)

        return inner_fun
    
    def _remove_job(func):

        def inner_func(self):
            if len(self.queue)==0:
                print()
                print("\nCurrently no job available")
                
                for i in range(self.maxlen):
                    if len(self.waiting)==0:
                        break
                    print("The job in the waiting state is moved in to the queue: ",self.waiting[0])
                    self.waiting.pop(0)
            else:
                func(self)
                print("\nThe job in the waiting state is moved in to the queue: ",self.waiting[0])
                self.waiting.pop(0)    


        return inner_func

    @_add_job
    def enqueue(self,value):
        self.queue.append(value)
    


    @_remove_job
    def dequeue(self):
        print("The dequeued element is :",self.queue[0])
        self.queue.pop(0)

    def front(self):
        if len(self.queue)==0:
            print("The queue is underflow")
            return 
        else:
            print("The front element is :",self.queue[0])

if __name__=="__main__":
    q=Queue(2)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(2)

    q.dequeue()

    q.front()