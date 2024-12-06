from typing import List

def xmas_count_2(grid: List[List[str]]) -> int:
    R, C = len(grid), len(grid[0])

    count = 0

    for r in range(R):
        for c in range(C):
            try:
                if (grid[r][c] == "A"
                    and grid[r-1][c-1] == grid[r+1][c-1] == "M"
                    and grid[r-1][c+1] == grid[r+1][c+1] == "S"
                ) or (
                    grid[r][c] == "A"
                    and grid[r-1][c-1] == grid[r+1][c-1] == "S"
                    and grid[r-1][c+1] == grid[r+1][c+1] == "M"
                ) or (
                    grid[r][c] == "A"
                    and grid[r-1][c-1] == "M" and grid[r+1][c-1] == "S"
                    and grid[r-1][c+1] == "M" and grid[r+1][c+1] == "S"
                ) or (
                    grid[r][c] == "A"
                    and grid[r-1][c-1] == "S" and grid[r+1][c-1] == "M"
                    and grid[r-1][c+1] == "S" and grid[r+1][c+1] == "M"
                ):
                    count += 1
            except:
                pass
    return count

# Too lazy to refactor this 🥱
def xmas_count(grid: List[List[str]]) -> int:
    R, C = len(grid), len(grid[0])

    count = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] == "X":
                # left
                if c >= 3 and "".join(grid[r][c-3:c+1]) == "SAMX":
                    count += 1
                # top left
                if c >= 3 and r >= 3:
                    s = True
                    if grid[r][c] != "X":
                        s = False
                    if grid[r-1][c-1] != "M":
                        s = False
                    if grid[r-2][c-2] != "A":
                        s = False
                    if grid[r-3][c-3] != "S":
                        s = False
                    if s:
                        count += 1
                # top
                if r >= 3:
                    if grid[r][c] == "X" and grid[r-1][c] == "M" and grid[r-2][c] == "A" and grid[r-3][c] == "S":
                        count += 1
                # top right
                if c <= C-4 and r >= 3:
                    s = True
                    if grid[r][c] != "X":
                        s = False
                    if grid[r-1][c+1] != "M":
                        s = False
                    if grid[r-2][c+2] != "A":
                        s = False
                    if grid[r-3][c+3] != "S":
                        s = False
                    if s:
                        count += 1
                # right
                if c <= C-4:
                    count = count + 1 if "".join(grid[r][c:c+4]) == "XMAS" else count
                # bottom right
                if c <= C-4 and r <= R-4:
                    s = True
                    if grid[r][c] != "X":
                        s = False
                    if grid[r+1][c+1] != "M":
                        s = False
                    if grid[r+2][c+2] != "A":
                        s = False
                    if grid[r+3][c+3] != "S":
                        s = False
                    if s:
                        count += 1
                # bottom
                if r <= R-4:
                    if grid[r][c] == "X" and grid[r+1][c] == "M" and grid[r+2][c] == "A" and grid[r+3][c] == "S":
                        count += 1
                # bottom left
                if c >= 3 and r <= R-4:
                    s = True
                    if grid[r][c] != "X":
                        s = False
                    if grid[r+1][c-1] != "M":
                        s = False
                    if grid[r+2][c-2] != "A":
                        s = False
                    if grid[r+3][c-3] != "S":
                        s = False
                    if s:
                        count += 1
    return count

if __name__ == "__main__":

    file_path = '2024/04/04_input.txt'
    input = []

    ans = 0
    with open(file_path, 'r') as file:
        for line in file:
            input.append(line)
    
    grid = []

    for i, line in enumerate(input):
        if i != len(input) - 1:
            grid.append(list(line)[:-1])
        else:
            grid.append(list(line))

    print("The output for part 1 is ", xmas_count(grid))
    print("The output for part 2 is ", xmas_count_2(grid))