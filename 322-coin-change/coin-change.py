class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dp(coins, amount):
            if amount in cache:
                return cache[amount]

            minimum = float('inf')

            if amount == 0:
                return 0
            
            if amount < 0:
                return float('inf')
            
            for coin in coins:
                minimum = min(1 + dp(coins, amount - coin), minimum)

            cache[amount] = minimum
            return minimum
        
        answer = dp(coins, amount)
        return -1 if answer == float("inf") else answer

