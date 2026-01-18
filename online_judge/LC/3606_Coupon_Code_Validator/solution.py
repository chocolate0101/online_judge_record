# link of the problem: https://leetcode.com/problems/coupon-code-validator/

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans = []
        for i in range(len(code)):
            if businessLine[i] not in ('electronics', 'grocery', 'pharmacy', 'restaurant'):
                continue
            
            if not isActive[i]:
                continue

            pattern = r'[A-Za-z0-9_]+$'
            if not re.match(pattern, code[i]):
                continue
            
            ans.append([businessLine[i], code[i]])

        ans.sort()
        return [n[1] for n in ans]