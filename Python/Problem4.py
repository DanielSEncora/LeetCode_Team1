class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenS = len(s)
        lenP = len(p)
        def match(indexS: int = 0, indexP: int = 0):
            isPastStr = indexS >= lenS

            if indexP >= lenP:
                return isPastStr

            #For characters with *
            if indexP < lenP - 1 and p[indexP + 1] == '*' :
                if match(indexS, indexP + 2):
                    return True
                if not isPastStr and p[indexP] in {'.', s[indexS]}:
                    return match(indexS + 1, indexP)
            #For solo characters
            elif not isPastStr and p[indexP] in {'.', s[indexS]}:
                return match(indexS + 1, indexP + 1)

            return False
        
        return match()