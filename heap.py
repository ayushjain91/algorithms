#   Defines the heap class
#   The class creates a min-heap based on key
#   Also provides functionality to search items by value
#       - value must be hashable

class heap:
    
    def __init__(self, arr = [], key = lambda x:x[0], value = lambda x:x[1]):
    # Creates a heap out of list arr using key and value functions
    # If no argument is provided, creates an empty heap
        self.heapArr = arr
        self.valtoIndex = {}
        self.func_val = value
        self.func_key = key
    
    def isEmpty(self):
    # Checks if heap is empty
        return len(self.heapArr) == 0
    
    def addElement(self, element):
    # Adds an element to the heap
        self.heapArr.append(element)
        self.valtoIndex[self.func_val(element)] = len(self.heapArr)-1
        self.bubbleUp(len(self.heapArr)-1)
        
    def bubbleUp(self, ind):
        
        parent = (ind - 1)/2
        child = ind
        while(child!=0 and self.func_key(self.heapArr[child])<self.func_key(self.heapArr[parent])):
            self.heapArr[child], self.heapArr[parent] = self.heapArr[parent], self.heapArr[child]
            self.valtoIndex[self.func_val(self.heapArr[child])] = child
            self.valtoIndex[self.func_val(self.heapArr[parent])] = parent
            
            child = parent
            parent = (child -1)/2
            
        
    def removeElement(self,value):
        # Removes and returns the element with specific value
        assert len(self.heapArr) == len(self.valtoIndex)
        idx = self.valtoIndex[value]
        lastElement = self.heapArr.pop()
        del self.valtoIndex[value]
        if len(self.heapArr)==idx:
            return lastElement
        element = self.heapArr[idx]
        
        self.heapArr[idx] = lastElement
        self.valtoIndex[self.func_val(lastElement)] = idx
        
        self.bubbleUp(idx)
        self.bubbleDown(idx)
        assert len(self.heapArr) == len(self.valtoIndex)
        return element
        
    def bubbleDown(self, ind):
        
        _length = len(self.heapArr)
        curr = ind
        child = 2*curr + 1
        if (_length>2*curr+2):
            if self.func_key(self.heapArr[2*curr+1])>self.func_key(self.heapArr[2*curr+2]):
                child = 2*curr + 2
        while(child<len(self.heapArr)-1 and self.func_key(self.heapArr[child])<self.func_key(self.heapArr[curr])):
            self.heapArr[curr], self.heapArr[child] = self.heapArr[child],self.heapArr[curr]
            self.valtoIndex[self.func_val(self.heapArr[child])] = child
            self.valtoIndex[self.func_val(self.heapArr[curr])] = curr
            
            curr = child
            if (len(self.heapArr)>2*curr+2) and self.func_key(self.heapArr[2*curr+1])>self.func_key(self.heapArr[2*curr+2]):
                child = 2*curr + 2
            else:
                child = 2*curr + 1
            
                
    def pop(self):
        #   Removes and returns the minimum key element in the heap
        assert len(self.heapArr) == len(self.valtoIndex)
        minElement = self.heapArr[0]
        del self.valtoIndex[self.func_val(minElement)]
        lastElement = self.heapArr.pop()
        if len(self.heapArr)!=0:
            self.heapArr[0] = lastElement
            #print self.heapArr
            self.valtoIndex[self.func_val(lastElement)] = 0
        
            self.bubbleDown(0)
        
        assert len(self.heapArr) == len(self.valtoIndex)
        return minElement
    
   
        
if __name__ == '__main__':
    value = lambda x:x[3]
    pq = heap(key = lambda x:x[2], value = lambda x:x[3])
    for i in range(10):
        pq.addElement([1,2,10-i,10-i])
        print 'Inserted element', 10-i
        
    for i in range(10):
        print 'Minimum element', value(pq.pop()), 'deleted' 
        
        
            
        