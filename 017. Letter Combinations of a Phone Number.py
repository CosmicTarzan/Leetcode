class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
          '2': 'abc',
          '3': 'def',
          '4': 'ghi',
          '5': 'jkl',
          '6': 'mno',
          '7': 'pqrs',
          '8': 'tuv',
          '9': 'wxyz'
        }
        ans = []
        def recurse(possibilities, remaining):
          if remaining == '':
            ans.append(possibilities)
          else:
            for letter in d[remaining[0]]:
              recurse(possibilities + letter, remaining[1:])
        
        if digits == '':
            return ans
        
        recurse('', digits)
        return ans
