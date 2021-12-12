class IslandFinder:
    # Courtesy of https://medium.com/analytics-vidhya/number-of-islands-day-5-python-5c12783515b2
    min_island_size = 49
    current_island_size = 0
    new_island = False

    def __init__(self, grid):
        self.grid = grid

    def isSafe(self, grid, row, col, visited):
        return(0 <= row < len(grid) and
               0 <= col < len(grid[0]) and
               grid[row][col] == 0 and visited[row][col] == False)

    def dfs(self, row, col, visited, grid):
        valid_row = [-1, 0, 0, 1]
        valid_col = [0, -1, 1, 0]
        visited[row][col] = True
        for neighbour in range(len(valid_row)):
            new_row = row + valid_row[neighbour]
            new_col = col + valid_col[neighbour]
            if(self.isSafe(grid, new_row, new_col, visited)):
                self.current_island_size += 1
                self.dfs(new_row, new_col, visited, grid)

    def get_min_island_size(self):
        visited = [[False for col in range(len(self.grid[0]))]
                   for row in range(len(self.grid))]
        count = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if(self.grid[row][col] == 0 and visited[row][col] == False):
                    self.current_island_size = 1
                    self.dfs(row, col, visited, self.grid)
                    self.min_island_size = min(
                        self.min_island_size, self.current_island_size)
                    count += 1
        return self.min_island_size
