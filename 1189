class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = collections.defaultdict(int)

        for char in text:
            if char in 'balon':
                hashmap[char] += 1

        output = float("inf")

        for char in 'balon':
            if char == 'o' or char == 'l':
                output = min(output, hashmap[char]//2)
            else:
                output = min(output, hashmap[char])

        return output
