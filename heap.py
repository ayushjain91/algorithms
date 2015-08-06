
#   Defines the heap class
#   Each element of a heap is [key,value] pair
#   The class creates a min-heap based on key
#   Also provides functionality to search items by value
#       - value must be hashable

class heap:
    
    def __init__(self, arr = []):
    # Creates a heap
    # If no argument is provided, creates an empty heap
        self.heapArr = arr
        self.valtoIndex = {}
    
    def isEmpty(self):
    # Checks if heap is empty
        return len(self.heapArr) == 0
    
    def addElement(self, pair):
    # Adds an element to the heap
    # pair is of the form [key, value]
        self.heapArr.append(pair)
        self.valtoIndex[pair[1]] = len(self.heapArr)-1
        self.bubbleUp(len(self.heapArr)-1)
        
    def bubbleUp(self, ind):
        
        parent = (ind - 1)/2
        child = ind
        while(child!=0 and self.heapArr[child][0]<self.heapArr[parent][0]):
            self.heapArr[child], self.heapArr[parent] = self.heapArr[parent], self.heapArr[child]
            self.valtoIndex[self.heapArr[child][1]] = child
            self.valtoIndex[self.heapArr[parent][1]] = parent
            
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
        self.valtoIndex[lastElement[1]] = idx
        
        self.bubbleUp(idx)
        self.bubbleDown(idx)
        assert len(self.heapArr) == len(self.valtoIndex)
        return element
        
    def bubbleDown(self, ind):
        
        _length = len(self.heapArr)
        curr = ind
        child = 2*curr + 1
        if (_length>2*curr+2):
            if self.heapArr[2*curr+1][0]>self.heapArr[2*curr+2][0]:
                child = 2*curr + 2
        while(child<len(self.heapArr)-1 and self.heapArr[child][0]<self.heapArr[curr][0]):
            self.heapArr[curr], self.heapArr[child] = self.heapArr[child],self.heapArr[curr]
            self.valtoIndex[self.heapArr[child][1]] = child
            self.valtoIndex[self.heapArr[curr][1]] = curr
            
            curr = child
            if (len(self.heapArr)>2*curr+2) and self.heapArr[2*curr+1][0]>self.heapArr[2*curr+2][0]:
                child = 2*curr + 2
            else:
                child = 2*curr + 1
            #print self.heapArr, curr, child,
                
    def pop(self):
        #   Removes and returns the minimum key element in the heap
        assert len(self.heapArr) == len(self.valtoIndex)
        minElement = self.heapArr[0]
        del self.valtoIndex[minElement[1]]
        lastElement = self.heapArr.pop()
        if len(self.heapArr)!=0:
            self.heapArr[0] = lastElement
            #print self.heapArr
            self.valtoIndex[lastElement[1]] = 0
        
            self.bubbleDown(0)
        
        assert len(self.heapArr) == len(self.valtoIndex)
        return minElement
    
   
        
if __name__ == '__main__':
    pq = heap()
    for i in range(10):
        pq.addElement([10-i,10-i])
        print 'Inserted element', 10-i
        
    for i in range(10):
        print 'Minimum element', pq.pop()[0], 'deleted' 
        
        
            
        