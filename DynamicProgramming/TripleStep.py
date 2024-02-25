class TripleStep:
    def solution(self, n:int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0]=1
        dp[1]=2
        dp[2]=3
        for i in range(3,n):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n-1]

c = TripleStep()
print(c.solution(10))

            
    