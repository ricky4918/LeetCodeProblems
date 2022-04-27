class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        



        copy = [[0] * n] * m

        for i in range(m):

            copy[i][0] = 1
        for j in range(n):

            copy[0][j] = 1


        for x in range(1, m):
            for y in range(1,n):

                copy[x][y] = copy[x][y-1] + copy[x-1][y]

        return copy[-1][-1]