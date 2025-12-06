### Part 1

***Problem:***
- The puzzle input consists of ranges of numbers representing IDs
- Any given ID can be either valid or invalid
- An ID is invalid if the first half of its digits are identical to the second half (e.g. `1313` or `64836483`)
- What is the sum of invalid IDs across all ranges?

***Approach:***
- Parse the input and store the ranges as an array of tuples `list[tuples[int, int]]`
- Initialize a variable `invalid` representing the sum of invalid IDs
- Iterate all integers from 1 to the largest possible one that could still fit into one of the ranges if its digits were repeated
- _Observation:_ the largest upper boundary of a range has 10 digits, therefore the largest possible repeatable number will be under 100,000
- For each integer build the potential invalid ID `candidate` by repeating its digits
- Iterate the ranges and check if `candidate` falls into the range and if so, add its value to `invalid`
- After the loop return `invalid`

---

### Part 2

***Problem:***
- Same basic problem but now the definition of an invalid ID is broader
- Any number that represents a repeated smaller number any number of times is considered an invalid ID
- For example 141414 is the number 14 repeated 3 times, or 5555555 is the number 5 repeated 7 times

***Approach:***
- _Observation:_ there now is a danger of duplication: 2222 can be created by repeating the number 2 four times or the number 22 twice
- To avoid counting the same invalid ID twice, initialize `invalid` as a `set` instead of a number
- The same outer loop as in part 1, but now we add another inner loop which increments the repetition factor `repeat`
- `repeat` must be at least 2 and at most 10 (although the upper boundary shrinks as digits increase => optimize by exiting the loop early)
- For each combination of `i` and `repeat` create a potential `candidate`
- If a candidate falls within one of the ranges add it to the set `invalid`
- After the loop return the sum of all IDs in the set
