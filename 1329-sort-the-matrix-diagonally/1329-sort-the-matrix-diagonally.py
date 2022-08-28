class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            c = 0
            tmp = []
            for j in range(min(m-i, n)):
                tmp.append(mat[i + c][j])
                c += 1
                
            tmp.sort()
            c = 0
            for j in range(min(m-i, n)):
                mat[i + c][j] = tmp[c]
                c += 1
        
        for i in range(1, n):
            c = 0
            tmp = []
            for j in range(min(n-i, m)):
                print(j, i+c)
                tmp.append(mat[j][i+c])
                c += 1
                
            tmp.sort()
            c = 0
            for j in range(min(n-i, m)):
                mat[j][i+c] = tmp[c]
                c += 1
        
        return mat