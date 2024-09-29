from functools import reduce
#region 1

def unique_in_order(s):
    res = []
    for i in range(len(s)):
        if len(s) == 0:
            res = []
            
        if len(s) == 1:
            res.append(s[i])

        elif s[i] != s[i - 1]:
            res.append(s[i])
    return res

#print(unique_in_order('AAAABBBCCDAABBB'))
#print(unique_in_order('ABBCcAD'))
#print(unique_in_order([1, 2, 2, 3, 3]))
#print(unique_in_order((1, 2, 2, 3, 3)))

#region 2

def multiples(n):
    list = []
    if n < 0:
        return 0
    for k in range(n):
        if k % 3 == 0 and k not in list:
            list.append(k)
        if k % 5 == 0 and k not in list:
            list.append(k)
    return sum(list)

def solution(n):
    return sum(k for k in range(n) if k % 3 == 0 or k % 5 == 0)

def sol2(n):
    list = []
    for k in range(n):
        if k % 3 == 0 or k % 5 == 0:
            list.append(k)
    return sum(list)

#region 3

def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:]

#print(maskify('4556364607935616'))

#region 4

def persistence(num):
    count = 0
    while len(str(num)) > 1:
        num = reduce(lambda x, y: x * y, [int(x) for x in str(num)])
        count += 1
    return count

#print(persistence(39))

#region 5

def number(bus_stops):
    return sum([x[0] - x[1] for x in bus_stops])

#print(number([[10,0],[3,5],[5,8]]))

#region 6

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

#region 7

def find_short(s):
    res = len(s.split()[0])
    for x in s.split():
        if len(x) < res:
            res = len(x)
    return res

# alt

def find_shorts(s):
    return min(len(x) for x in s.split())

#region 8
def array_diff(a,b):
    return [x for x in a if x not in b]

#region 9
def stringMatching(words):
    result = []
    for word in words:
        for i in words:
            if word in i and word != i:
                result.append(word)
                break
    return result

#region 10
def oddnumber(num):
    i = len(num) - 1
    while i >= 0:
        if int(num[i])%2 != 0:
            return num[:i+1]
        i -= 1
    return ''

#region 11
def twoSum(nums, target):
    for i in range(len(nums) - 1): # el -1 es para optimizar y que no itere una vez mas al pedo
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []