class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        number_black = 0
        hashmap_row = defaultdict(int)
        hashmap_column = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    hashmap_column[j] += 1 
                    hashmap_row[i] += 1

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and hashmap_column[j] == 1 and hashmap_row[i] == 1:
                    number_black += 1

        return number_black
