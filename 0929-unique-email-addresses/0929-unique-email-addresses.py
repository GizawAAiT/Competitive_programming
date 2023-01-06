class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            local, domain = emails[i].split('@')
            local = ''.join((local.split("+")[0]).split('.'))
            emails[i] = '@'.join([local, domain]) 
        return len(set(emails))