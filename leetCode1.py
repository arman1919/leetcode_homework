# 1. Two Sum
#
# def foo(ls,numb):
#     for i in ls:
#         for j in ls:
#             if i+j == numb:
#                 return (ls.index(i),ls.index(j))
#
#
# ls = [1,2,3,4,5,6]
# target = 9
# print(foo(ls,target))

# 121. Best Time to Buy and Sell Stock

# def maxProfit(prices):
#
#     maximum = 0
#     for i in range(len(prices)):
#         for j in range(i,len(prices)):
#             if maximum > prices[i] - prices[j]:
#                 maximum = prices[i] - prices[j]
#                 day1 = prices[i]
#                 day2 = prices[j]
#
#     return abs(maximum)
#
#
# prices = [7,1,5,3,6,4]
#
# print(maxProfit(prices))
#
# prices2 = [7,6,4,3,1]
#
# print(maxProfit(prices2))


# 217. Contains Duplicate

# def dubl(ls):
#     count = 0
#     for i in ls:
#         for j in ls:
#             if j == i:
#                 count += 1
#             if count == 2:
#                 return False
#         count = 0
#     return True
#
# ls = [1,2,3,4,5,7,8]
#
# print(dubl(ls))
#
# ls = [1,2,3,4,5,7,8,8]
#
# print(dubl(ls))

# def summ (a,b):
#     ls = []
#     for i in range(a):
#         ls.append(i)
#     for i in  range(b):
#         ls.append(i)
#
#     return len(ls)
#
#
# y = 5
# x = 4
# print(summ(x,y))

# 191. Number of 1 Bits


# def count1(n):
#     count = 0
#     while n !=0:
#         if n % 2 == 1:
#             count +=1
#         n //= 2
#     return count
#
# n = 0b010001000100
#
# print(count1(n))


# 190. Reverse Bits

# def Reverse(n):
#     ls = []
#     while n != 0:
#
#         ls . append(n%2)
#         n //= 2
#
#     numb = 0
#     i = len(ls)-1
#     j = 0
#     while i >= 0:
#         numb += ls[i]*(2**j)
#         i -= 1
#         j += 1
#     return numb
#
# n =  0b100101
#
# print(Reverse(n))


# 53. Maximum Subarray

# def maxsubarray(nums):
#     maxsum = nums[0]
#     currentsum = nums[0]
#     for i in range(1, len(nums)):
#         currentsum = max(nums[i], currentsum + nums[i])
#         maxsum = max(maxsum, currentsum)
#     return maxsum
#
#
# nums =[-2,1,-3,4,-1,2,1,-5,4]
#
# print(maxsubarray(nums))

