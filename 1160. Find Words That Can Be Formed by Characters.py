class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        score = 0
        checkDict = {}
        for c in chars:
            if c in checkDict.keys():
                checkDict[c] += 1
            else:
                checkDict[c] = 1
        for word in words:
            wordDict = {}
            for c in word:
                if c in wordDict.keys():
                    wordDict[c] += 1
                else:
                    wordDict[c] = 1
            inner = True
            for c in wordDict.keys():
                if c in checkDict.keys():
                    if wordDict[c] > checkDict[c]:
                        inner = False
                        break
                else:
                    inner = False
                    break
            if inner:
                score += len(word)
        return score
