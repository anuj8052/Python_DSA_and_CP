# basic python question
# Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms) 

# gfg code

class Solution:

    def seriesSum(self, n):
        sum = 0

        sum = int(n*(n+1)/2)

        return sum