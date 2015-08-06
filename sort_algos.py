import random

def selection(arr, idx, lo = 0, hi = None, key = lambda x:x):
#   Returns the idx-th order element in arr[lo] to arr[hi]
#   Complexity: O(n) on average
    if hi == None:
        hi = len(arr) - 1
    if idx > hi - lo + 1 or idx <= 0:
        raise SyntaxError('The order of the element to be found must be <= the length of the array and >= 0')
    if hi == lo:
        return lo
    r = random.randint(lo, hi)
    arr[lo], arr[r] = arr[r], arr[lo]
    pivot = arr[lo]
    i = lo + 1
    for j in range(lo+1,hi+1):
        if key(arr[j])<=key(pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[lo], arr[i-1] = arr[i-1], arr[lo]
    if idx == i-lo:
        return arr[i-1]
    elif idx > i - lo:
        return selection(arr, idx - i + lo , i, hi)
    else:
        return selection(arr, idx, lo, i-1)
    
def quickSort(arr, lo = 0, hi = None, order = 'ascending', key = lambda x:x):
#   Sorts the array arr in-place using quicksort
#   Runtime: O(n*log(n)) on average
    if hi == None:
        hi = len(arr) - 1
    _quickSort(arr, lo, hi, key)
    if order == 'descending':
        arr.reverse()
    
def _quickSort(arr, lo = 0, hi = None, key = lambda x:x):
#   Sorts the array arr in-place using quicksort
#   Runtime: O(n*log(n)) on average
    if hi<=lo:
        return
    r = random.randint(lo, hi)
    arr[lo], arr[r] = arr[r], arr[lo]
    pivot = key(arr[lo])
    i = lo + 1
    for j in range(lo+1,hi+1):
        if key(arr[j])<=pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[lo], arr[i-1] = arr[i-1], arr[lo]
    _quickSort(arr, lo, i-2)
    _quickSort(arr, i, hi)

def mergeSort(arr, start = 0, end = None, sort = 'ascending', key = lambda x:x):
#   Sorts the array arr using mergesort - arr is modified
#   Returns the number of inversions in arr
#   Runtime: O(n*log(n))
    if end == None:
        end = len(arr)-1
    if start == end:
        return 0
    mid = (start+end)/2
    inversions = mergeSort(arr,start,mid, key)
    inversions += mergeSort(arr, mid + 1, end, key)
    inversions += merge(arr, start, mid, end, key)
    
    return inversions

def merge(arr, start, mid, end, sort = 'ascending', key = lambda x:x):
    a = [0 for i in range(start,end+1)]
    p1 = start
    p2 = mid+1
    inversions = 0
    k = 0
    while(p1<=mid and p2<=end):
        if key(arr[p1])<=key(arr[p2]):
            a[k] = arr[p1]
            k += 1
            p1 += 1
        else:
            inversions += mid - p1 + 1
            a[k] = arr[p2]
            p2 += 1
            k += 1
    while (p1<=mid):
        a[k] = arr[p1]
        k += 1
        p1 += 1
    while (p2<=end):
        a[k] = arr[p2]
        p2 += 1
        k += 1
    
    if sort == 'descending':
        a.reverse()
    arr[start:end+1] = a
    return inversions


  
import random
arr = [random.randint(0,10000000) for i in range(1000000)]
quickSort(arr)

for i in range(len(arr)-1):
    assert arr[i+1]>=arr[i]
print 'Sorted an array of size 1000000'

arr = [100-i for i in range(100)]
print selection(arr, 20)
