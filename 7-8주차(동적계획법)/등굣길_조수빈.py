def solution(m, n, puddles):
    answer = 0
    memo = [[0 for i in range(m)] for j in range(n)]
    
    for i in range(0,n):
        for j in range(0,m):
            if [j+1,i+1] in puddles:
                memo[i][j] = 0
            elif i != 0 and j !=0:
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
            elif i == 0 and j!=0:
                memo[i][j] = memo[i][j-1]
            elif j == 0 and i!= 0:
                memo[i][j] = memo[i-1][j]
            else:
                memo[0][0] = 1
                
    answer = memo[-1][-1] % 1000000007
    return answer
