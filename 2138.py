class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)

        ans = [s[i:i+k] for i in range(0, n, k)]
        if n % k == 0: return ans
        ans[-1] += fill *(k - (n % k))


        return ans
        
