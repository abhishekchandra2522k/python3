class Solution:
    def nCr(self, n, r):
        return (self.fact(n) // (self.fact(n-r) * self.fact(r))) % 1000000007 
    
    def fact(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.nCr(n,r))