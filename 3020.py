class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 1

        for key in count.keys():
            if key == 1:
                total = count[key] if count[key] % 2 else count[key] - 1
            else:
                total = 1

                while count[key] >= 2 and key*key in count:
                    total += 2
                    key = key * key

            ans = max(total, ans)


        return ans
