class StringIterator:

    def __init__(self, compressedString: str):
        self.letter = []
        self.value = []
        i = 0
        j = 1

        while j < len(compressedString):
            val = 0
            while j < len(compressedString) and compressedString[j].isnumeric():   
                val = (val * 10) + int(compressedString[j])
                j += 1
            self.letter.append(compressedString[i])
            self.value.append(val)
            i = j
            j += 1

        # print(self.letter, self.value)
        self.curr = 0


    def next(self) -> str:
        if self.curr == len(self.letter):
            return " "
        self.value[self.curr] -= 1
        ans = self.letter[self.curr]
        if self.value[self.curr] == 0:
            self.curr += 1
        return ans
        

    def hasNext(self) -> bool:
        if self.curr == len(self.letter):
            return False
        else:
            return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
