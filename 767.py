class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = collections.Counter(s)

        max_count = 0
        max_char = ""

        for char, count in char_counts.items():
            if count > max_count:
                max_count = count
                max_char = char

        if max_count > (len(s) + 1) // 2:
            return ""

        ans = [""] * len(s)
        index = 0

        for _ in range(max_count):
            ans[index] = max_char
            index += 2
            char_counts[max_char] -= 1

        for char, count in char_counts.items():
            while count > 0:
                if index > len(s) - 1:
                    index = 1
                ans[index] = char
                index += 2
                count -= 1

        return "".join(ans)


