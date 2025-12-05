### Part 1

***Problem:***
- We imagine a circular array with 100 positions endlessly repeating and numbered 0 to 99 
- We start at position 50
- The puzzle input consists of instructions about where to move on the circle
- L23 means move left 23 steps, R1 means move right 1 step
- Each instruction starts at the position to which the last one pointed 
- How many times will an instruction point us towards the number 0?

***Approach:***
- Initialize the variables `current_position` and `landed_on_zero`
- Iterate the instructions and parse the direction and steps
- If the direction is `L` then subtract, if it's `R` then add the steps to the current position
- Use modulo `% 100` to make sure the new position stays within the range
- Check whether the new position is zero and if so increment `landed_on_zero`
- After the loop return `landed_on_zero`

---

### Part 2

***Problem:***
- Now we don't just want to know whether an instruction causes us to land on 0 directly but also how many times we came across 0 in passing

***Approach:***
- Same variable initializations, same outer loop
- Take the `divmod` of the step count in order to extract the number of `full_rotations` and to reduce `steps` to a number under 100
- `full_rotations` can be added to `landed_on_zero` directly
- Instead of updating the `current_position` immediately, put `new_postion` (without modulo) in a separate variable
- In addition to `full_rotations` we can increment `landed_on_zero` if two conditions are met: 
    1. we start in the range 1 - 99 and 
    2. we end up outside of that range
- Update `landed_on_zero` accordingly
- Now apply the modulo and update `current_position`
- After the loop return `landed_on_zero`
