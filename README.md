# advent-2024

Yet another Advent of Code 2024 repository

## Solution Sketches
### Day 1
1. Implementation (sum absolute values of sorted lists)
2. Implementation; I build a dictionary to easily look up the number of occurrences of a number (this is mild overkill for the problem size).
### Day 2
1. I check first that the differences between adjacent values are valid, and then check that the sequence is monotonic.
2. Brute-force over all possible removals (as well as no removals)
### Day 3
1. I use a cursed checking function to look for the multiplication commands
2. Add in an enable flag to turn on and off multiplications
### Day 4
1. Search for `XMAS` in all 8 directions
2. Look for all the `A`s and match `M` and `S` across them diagonally
### Day 5
1. Brute force rule checking (index both numbers and check if the rule holds)
2. Construct an adjacency list from the conditions and build a topological sorting
### Day 6
1. Use a set to store previously visited positions, and simulate until we run out of bounds
2. For every position, check for infinite loops (if we ever end up in the same position and direction). This code could probably be optimized, but hey it runs :D
### Day 7
1. Recursively brute force all possible combinations of operations.
2. Also recursively brute force all possible combinations of operations (but add the third operation).
### Day 8
1. For each pair with the same frequency, we can calculate the two antinodes by considering the two cases (whether the slope formed by the two antennas is positive or negative) and finding the appropriate distances from there. Mild black magic geometry used. A set stores positions to account for overlapping.
2. We iterate through all multiples of the previously calculated distances.
### Day 9
1. Generate the expanded disk layout while storing the location of each empty space, then iterate backwards from the end to fill in the empty spaces until there is no benefit to doing so.
2. Similar approach, but with storing empty blocks (whose size shrinks as they're filled up) instead.
### Day 10
1. Run a BFS from each 0 node, using a set to keep track of visited nodes
2. The input is small enough that we can simply disable the visited node check
### Day 11
1. Simulation, repeatedly regenerating the stones according to the rules. We use a dictionary (storing the quantity of each stone number) to prevent repeated computation.
2. Because of the efficiency from the dictionary, we simply increase the iteration count.
### Day 12
1. Floodfill to get the cells in each region. Then, count the perimeter by subtracting edges that are between two cells.
2. The number of sides is equal to the number of corners. I bash the number of corners that each cell has by checking all locations of corners (both outside/convex and inside/concave corners).
### Day 13
1. After regex parsing, bash the number of button presses. The solution seems to be unique.
2. Solve the system of linear equations with numpy. Due to numerical imprecision, I had to round numpy's outputs.
### Day 14
1. Implementation (slight speedup by directly calculating end positions with modulo instead of simulation)
2. Floodfill each frame. If the frame contains a Christmas tree, it should contain a large contiguous region.