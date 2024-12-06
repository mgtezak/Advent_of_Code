### Part 1

***Problem:***
- There's a 2-dimensional grid with empty space `.`, obstacles `#` and a single upwards pointing arrow `^`
- A guard starts traversing the grid starting at the arrow and moving upwards
- When he hits an obstacle he turns 90° right and continues walking until he exits the grid
- How many squares will the guard have traversed before he exits?

***Approach:***
- Parse the puzzle input to get the grid, its length and width and starting coordinates
- Create an array named `direction` representing the four directions up, right, down and left (the exact order in which the guard will change direction)
- Create another variable `d` which will track the current direction (it could either represent the current index of the direction array or the actual direction itself using `itertools.cycle` on the directions)
- Initialize a set named `visited` to track the coordinates that the guard has traversed
- Create a loop in which the current directional coordinates are added to the current coordinates
    - If the resulting coordinates represent empty space inside the grid then add the new coordinates to `visited` and move forward
    - If they fall on an obstacle, then simply change direction by incrementing `d` (if `d` represents an index, you'll need to use modulo to avoid indexing errors)
    - If the resulting new coordinates are outside of the grid then break the loop
- Once the loop has terminated return the length of `visited`

---

### Part 2

***Problem:***
- We want to trap the guard in a loop, so that he never exits the grid 
- To achieve this, we are allowed to add an obstacle
- How many ways are there to trap the guard in a loop by adding a single obstacle?

***Approach:***
- The general idea will be to treat the `visited` set from part 1 as a list of candidates; you can add an obstacle to each of them individually and check whether a loop occurs
- Since the list of candidates will be somewhat large (for me more than 4500) it's wise to make some adjustments that will speed up grid traversal considerably even if they also make the code more verbose and complex:
    - Instead of taking a single step forward, you'll simply jump to the next obstacle using a function named `move`
    - This function obviously needs to take in the current position and direction but it also needs to accept `obstacles` dynamically, since you'll be adding and removing obstacles a lot
    - You'll want to be able to access a list of the current row's obstacles (i. e. their column indices) and quickly figure out, which will be the closest to the current column index
    - An efficient way to achieve this is to store the obstacles in two hashmaps: one will keep a list of column indices for each row the other a list of row indices for each column
    - Depending on the current direction you'll want to find the next smaller or next larger element in your list of obstacles, so it helps to have these lists sorted (`bisect.insort` provides an easy way to add a number to a `list` while keeping the list sorted)
    - Another (perhaps slightly unnecessary) optimization when scanning a sorted list is to use binary search (fortunately you don't have to write the binary search algorithm yourself, just use `bisect.bisect`)
    - To put it all together: the `move` function will check the current direction, retrieve the relevant list of obstacles, determine the closest obstacle in the current direction, determine the coordinates of the empty space right before it, and return the new coordinates and the updated direction 
- You can either use this new `move` function or the approach from part 1 to attain the list of `candidates`
- Once you have your list of candidates you'll need another function `is_looping`:
    - This function will determine whether or not a grid with a given collection of `obstacles` will result in the guard running in circles
    - Passig coordinates to this function isn't necessary since it'll always start from the original starting position 
    - In order to determine whether or not the path is looping, you'll need to store `visited` coordinates; you don't need to store the entire path in this set; it's enough to simply store the coordinates of turning points right before each obstacle
    - Use the `move` function inside a while loop and return `True` once a loop is detected or `False` once the coordinates are outside the bounds of the grid
- Finally, initialize a return variable `loop_count`, iterate the list of candidates and for each pair of coordinates do three things:
    - Add the coordinates to the two obstacle hashmaps
    - Check if the current collection of obstacles cause a loop to occur using `is_looping` and if so increment `loop_count`
    - Remove the coordinates from `obstacles` again
- Return `loop_count`