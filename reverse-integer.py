class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)
        number = 0
        remainder = 0
        arr = []
        while True:
            if n<10:
                arr.append(n)
                break
            remainder = n%10
            arr.append(remainder)
            n = n//10 
        for i in range(len(arr)-1,-1,-1):
            number = number + (arr[i]*(10**(len(arr)-1-i)))
        if x<0:
            if -1*number<=-2147483648:
                return 0
            else:
                return -1*number
        if number>2147483648:
            return 0
        else:
            return number
