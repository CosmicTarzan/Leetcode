class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor > 0):
          negative = True
          dividend = -dividend
        elif (divisor < 0 and dividend > 0):
          negative = True
          divisor = -divisor
        else:
          negative = False
          if dividend < 0:
            divisor = -divisor
            dividend = -dividend

        count = len(range(0, dividend+1, divisor))
    
        if negative:
          if - count + 1 <:
            return - 2**31
          return - count + 1
        if count - 1 > 2**31 - 1:
          return 2**31 - 1
        return count - 1

