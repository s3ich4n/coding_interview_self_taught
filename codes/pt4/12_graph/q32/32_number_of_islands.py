from typing import List


class Solution:
    @staticmethod
    def coord_is_out_of_range(
        grid: List[List[str]],
        x: int,
        y: int,
    ):
        # 가로길이, 세로길이에 각각 대응해야함에 유의!
        x_is_out_of_range = x < 0 or x >= len(grid)
        y_is_out_of_range = y < 0 or y >= len(grid[0])

        return (x_is_out_of_range or y_is_out_of_range)

    def dfs(
        self,
        grid: List[List[str]],
        x: int,
        y: int,
    ):
        # 더 이상 땅이 아닌 경우?
        if self.coord_is_out_of_range(grid, x, y) or grid[x][y] != '1':
            return

        # 다녀온 곳에 대해 '1'이 아닌 값으로 덮어쓴다.
        grid[x][y] = '#'

        self.dfs(grid, x+1, y)
        self.dfs(grid, x-1, y)
        self.dfs(grid, x, y+1)
        self.dfs(grid, x, y-1)

    def numIslands(
        self,
        grid: List[List[str]],
    ) -> int:

        # 예외처리
        if not grid:
            return 0

        count = 0

        # 가로길이, 세로길이에 각각 대응해야함에 유의!
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1

        return count


test1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

test2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "0"],
]


answer = Solution()
print(answer.numIslands(test1))
print(answer.numIslands(test2))
