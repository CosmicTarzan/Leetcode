class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d = {'N': [1, 0], 'S': [-1, 0], 'E': [0, 1], 'W': [0, -1]}
        pos = [0, 0]
        been = [pos[:]]
        for i in path:  
            for j in range(2):
                pos[j] = pos[j] + d[i][j]
            if pos in been:
                print(been)
                return True
            else:
                been.append(pos[:])
        return False
