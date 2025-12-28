def isPalindrome(self, x: int) -> bool:
    num = 0
    if x < 0:
        return False
    else:
        n = x
        l = len(str(x))
        for i in range(0, l):
            a = x % 10
            num = (num * 10) + a
            x = x // 10
        if (n == num):
            return True
        else:
            return False

