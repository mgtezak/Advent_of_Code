### Part 1

***Problem:***
- There's a two-dimensional grid with empty space represented by `.` and antennas represented by numbers or letters
- Some antennas share a frequency, meaning that they are represented by the same character (the letters are case-sensitive so `"a" != "A"` )
- Any time two antennas share a frequency, then there will appear "antinodes" on either side of the pair in such a way that they form a straight line of 4 equidistant points
- If an antinode falls outside the grid it doesn't count
- If it falls onto another antenna it will still count
- If two antinodes share coordinates they count as one
- How many unique antinode coordinates are there?

***Approach:***
- Parse the grid and its dimensions
- Create a hashmap `locations` where the keys represent a given antenna's unique character and the values represent the set of locations of this antenna type
- Initialize a set of `antinodes` 
- Iterate the antenna groups and within each group iterate the unique pairs of antennas (`itertools.combinations` is useful here)
- For each pair of antennas calculate the difference between their row indices `dr` and the difference between their column indices `dc`
- Add these differences to the coordinates of the first antenna and substract them from coordinates of the second one to get the locations of the two resulting antinodes
- If these locations fall within the bounds of the grid, add them to `antinodes`
- Finally return the length of `antinodes`

---

### Part 2

***Problem:***
- Instead of each antenna pair creating just two antinodes, they now create as many antinodes as can fit into the grid in evenly spaced intervals on their respective axis
- The locations of the antennas themselves also become antinodes
- How many unique antinode coordinates are there now?

***Approach:***
- Copy the approach from part 1 up to the point where you loop over each pair of antennas
- Again calculate the coordinate differences `dr` and `dc`
- Create a while loop that starts at the first antenna's coordinates
- In each iteration add the current coordinates to `antinodes` and the add the coordinate differences to the current coordinates
- The loop ends once the current coordinates are outside the bounds of the grid
- Create a while loop in the other direction starting at the second antenna, this time subtracting the differences
- Finally return the length of `antinodes`
