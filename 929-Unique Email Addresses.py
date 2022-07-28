import re
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        print (emails)
        ans = []
        for mail in emails:
            temp = mail.find("@")
            temp1 = mail[0:temp].replace(".","")
            temp2 = re.sub('\+[a-z]+', '', temp1)
            temp3 = mail[temp::]
            ans.append(temp2+temp3)
        return len(set(ans))