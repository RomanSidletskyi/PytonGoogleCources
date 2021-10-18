# List
## Iterating Over Lists Using Enumerate
When we covered for loops, we showed the example of iterating over a list. This lets you iterate over each element in the list, exposing the element to the for loop as a variable. But what if you want to access the elements in a list, along with the index of the element in question? You can do this using the enumerate() function. The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.

## List Comprehensions
You can create lists from sequences using a for loop, but there’s a more streamlined way to do this: list comprehension. List comprehensions allow you to create a new list from a sequence or a range in a single line.
For example, [ x*2 for x in range(1,11) ] is a simple list comprehension. This would iterate over the range 1 to 10, and multiply each element in the range by 2. This would result in a list of the multiples of 2, from 2 to 20.
You can also use conditionals with list comprehensions to build even more complex and powerful statements. You can do this by appending an if statement to the end of the comprehension. For example, [ x for x in range(1,101) if x % 10 == 0 ] would generate a list containing all the integers divisible by 10 from 1 to 100. The if statement we added here evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is, it gets added to the list.
List comprehensions can be really powerful, but they can also be super complex, resulting in code that’s hard to read. Be careful when using them, since it might make it more difficult for someone else looking at your code to easily understand what the code is doing.
```
list[i] = x Replaces the element at index i with x

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
-- Generate newfilenames as a list containing the new filenames
newfilenames = [e.replace('.hpp','.h') for e in filenames]

print(newfilenames) 
```
## Lists and Tuples Operations Cheat Sheet
Lists and tuples are both sequences, so they share a number of sequence operations. But, because lists are mutable, there are also a number of methods specific just to lists. This cheat sheet gives you a run down of the common operations first, and the list-specific operations second.

Common sequence operations
len(sequence) Returns the length of the sequence

for element in sequence Iterates over each element in the sequence

if element in sequence Checks whether the element is part of the sequence

sequence[i] Accesses the element at index i of the sequence, starting at zero

sequence[i:j] Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.

for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence at the same time

 Check out the [official documentation for sequence operations.](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

## List-specific operations and methods


list.append(x) Inserts x at the end of the list

list.insert(i, x) Inserts x at index i

list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.

list.remove(x) Removes the first occurrence of x in the list

list.sort() Sorts the items in the list

list.reverse() Reverses the order of items of the list

list.clear() Removes all the items of the list

list.copy() Creates a copy of the list

list.extend(other_list) Appends all the elements of other_list at the end of list

 Most of these methods come from the fact that lists are mutable sequences. For more info, see the [official documentation for mutable sequences and the list specific documentation.](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)

## List comprehension
[expression for variable in sequence] Creates a new list based on the given sequence. Each element is the result of the given expression.

[expression for variable in sequence if condition] Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true.  
