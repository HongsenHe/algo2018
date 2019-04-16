class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = {}
        res = 0
        
        for email in emails:
            email = email.split("@")
            local = email[0]
            domain = email[1]
            local = local.replace('.', '')
            local = local.split("+")
            head = local[0]
            if domain not in dic:
                dic[domain] = {head}
            else:
                if head not in dic[domain]:
                    dic[domain].add(head)

        for v in dic.values():
            res += len(v)
        return res
                
