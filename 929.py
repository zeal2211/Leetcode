class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        total = set()

        for email in emails:
            local = []

            for char in email:
                if char == '@' or char == '+':
                    break
                if char != '.':
                    local.append(char)

            domain = []
            for char in reversed(email):
                domain.append(char)
                if char == '@':
                    break
                

            local = ''.join(local)
            domain = ''.join(domain[::-1])
            print(local, domain)
            total.add(local + domain)

        return len(total)
