### Part 1

***Problem:***
- The puzzle input is a set of equations with a single number on the left and multiple numbers on the right 
- The numbers on the right are missing the operators between them
- How many lines can be made into valid equations by adding only `+` and `*` operators?

***Approach:***
- Create a function `is_valid` that takes in a target value (the left side of the equality) and a sequence of numbers (the right side)
- This could be solved recursively, but here's an iterative approach:
    - Initialize a queue that will hold tuples of the current index and the current value; the first tuple you'll add to it has the value of the first number and the index `1` (not `0` because the first number is already processed)
    - Now create a loop in which you pop any element (index/value pair) from the queue
    - Check if the popped index is within the bounds of the current list of numbers
    - If so, retrieve this next number and try combining it with the popped value either by addition or multiplication and add the resulting value back into the queue with an incremented index
    - If not, check whether the current value is equal to the target value
    - If it is, return `True`, if not `continue` popping elements from the queue
    - If the queue empties out, then that means that no matter how you set the operators, the equation will be invalid, so return `False`
    - [Optimization:] Before adding an element to the queue, check whether or not the value already exceeds the target, in which case skip it; since the puzzle input consists of only positive numbers we can be sure that further addition and multiplication will only increase the current value
- Parse the lines of the puzzle input, extracting the left and right side of each equation and feeding them into the `is_valid` function
- Keep track of the number of valid equations
- Return the the `total`

---

### Part 2

***Problem:***
- The same problem as in part 1 but now it's also possible to add a concatenation operator `||` between two numbers
- How many lines can now be made into valid equations?

***Approach:***
- You only need to add a single line to the `is_valid` function which concatenes the next number to the current value and pushes it into the queue