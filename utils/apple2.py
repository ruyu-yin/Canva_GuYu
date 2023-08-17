from collections import deque
from functools import reduce

add=[x**2 for x in range(5)]
print(add)

add2 = map(lambda  x: x**2,range(10))
print(list(add2))

def add1(x):return x**3
print(list(map(add1,range(3))))

def fun2(x):return x % 3 == 0 or x % 5 ==0
print(list(filter(fun2, range(2, 25))))

def add3(x,y):return x+y
print(reduce(add3, range(1, 11)))

list1 = [1,2,3]
queue= deque(list1)
print(queue.popleft())
print(queue)
print(queue.pop())
queue.remove(2)
print(queue)

