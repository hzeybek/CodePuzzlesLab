class TripleStep:
    def solution(self, n:int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 3
        
        dp = [0 for i in range(n+1)]
        dp[1]=1
        dp[2]=2
        dp[3]=3
        for i in range(4,n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]

    