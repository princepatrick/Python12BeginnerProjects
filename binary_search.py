import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l) - 1
    
    if low > high:
        return -1
    
    midpoint = (low + high) // 2

    if l[midpoint] == target :
        return midpoint
    elif l[midpoint] < target:
        return binary_search(l, target, midpoint+1, high)
    else:
        # l[midpoint] > target
        return binary_search(l, target, low, midpoint-1)
    
if __name__ == '__main__':
    
    length = 10000
    nums = []
    for i in range(length):
        nums.append(random.randint(-3*length, 3*length))
    nums.sort()

    start = time.time()
    for i in nums:
        naive_search(nums, i)
    end = time.time()
    print('Time for naive search is ',(end-start))

    start = time.time()
    for i in nums:
        binary_search(nums, i)
    end = time.time()
    print('Time for binary search is ',(end-start))
    
    '''
    nums = [2, 4, 5, 10, 12]

    print(naive_search(nums, 3))

    print(binary_search(nums, 3))
    '''
