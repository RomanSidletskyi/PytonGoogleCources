PEP : [Python Guidelines](https://peps.python.org/pep-0000/)
1. list Comprehensions : 
```
words = "test ttt rr".split()
[len(word) for word in words] --Comprehensions simple way to create new list
```
##list Comprehensions Syntax : `[expr(item) for item in iterable]`
##Equivalent Syntax : 
```
lengths = []
for word in words:
    lengths.append(len(word))
```   
```
from math import factorial
s = {len(str(factorial(x))) for x in range(20)} #create set
l = [len(str(factorial(x))) for x in range(20)] #create list
```
##Dict Comprehensions Syntax : `{key_expr(item): value_expr(item) for item in iterable}`

##Filtering Comprehensions:
```
from math import sqrt
def is_prime(x)
    if x < 2
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    
    [x for x in range(101) if is_prime(x)] #Filtering Comprehensions
    
```

##Generator Expressions : `(expr(item) for item in iterable)`
