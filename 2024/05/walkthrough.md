### Part 1

***Problem:***
- The puzzle input has two sections: "page ordering rules" and sequences of "page updates"
- Each line of the ordering rules constitutes a pair of numbers; the derived rule is that in any valid sequence the second number is never allowed to preceede the first one (not even if there is distance between them)
- The task is to identify the valid sequences, i. e. those that adhere to the ordering rules
- What is the sum of each valid sequence's middle page number?

***Approach:***
- Separate the two sections of the puzzle input
- Initialize a hashmap in which each key will correspond to a given page number und its value will correspond to the set of all page numbers that are not allowed to succeed it
- Iterate the lines of the first section (*page ordering rules*), extract each pair of numbers and add them to the hashmap
- Define a function `get_score` which determines the score of a given sequence from the second section (*page updates*)
    - Within this function initialize a set named `disallowed` which will keep track of page numbers that would break the ordering, if they appeared going forward
    - Iterate the sequence of page numbers, at each step checking whether the current page is still allowed and adding to the set of disallowed page numbers
    - If a given number is disallowed return 0; if the loop is able to conclude return the value of the middle page
- Use this function in the main scope by initializing a return variable `total`, iterating the lines of the second section and adding each line's score to the total
- Return `total`

--- 

### Part 2

***Problem:***
- We are no longer interested in the valid sequences but instead the invalid ones
- Each invalid sequence can be reordered such that it becomes valid
- What is the sum of each invalid sequence's middle page number after it has been made valid by reordering?

***Approach:***
- The only thing we need to modify from the first part's code is the `get_score` function
- This function now needs a boolean flag `is_reordered` to signify whether the sequence has already been reordered or not; you can set this flag to `False` by default since we start out by passing in unaltered sequences
- Instead of simply tracking the disallowed page numbers we track the exact index at which they became disallowed in a hashmap named `disallowed_after`
- Now, when iterating the sequence and a given page number is disallowed, retrieve its last valid index from the hashmap
- Use this index to create a new sequence called `reordered` in which the disallowed page number is moved to the correct position
- Then recursively feed the reordered sequence back into the `get_score` function, but this time with the boolean flag set to `True`
- At some point even a completely invalid sequence will be sufficiently reordered so that it becomes valid and the loop will run through uninterrupted
- Finally, all that's left is to check whether or not the sequence has been reordered at least once by checking `is_reordered` and to return either `0` or the middle value of the sequence
