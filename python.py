from functools import reduce
# 1

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

# 2

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

# 3

def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:]

#print(maskify('4556364607935616'))

# 4

def persistence(num):
    count = 0
    while len(str(num)) > 1:
        num = reduce(lambda x, y: x * y, [int(x) for x in str(num)])
        count += 1
    return count

#print(persistence(39))

# 5

def number(bus_stops):
    return sum([x[0] - x[1] for x in bus_stops])

#print(number([[10,0],[3,5],[5,8]]))

# 6

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

# 7

def find_short(s):
    res = len(s.split()[0])
    for x in s.split():
        if len(x) < res:
            res = len(x)
    return res

# alt

def find_shorts(s):
    return min(len(x) for x in s.split())

# 8
def array_diff(a,b):
    return [x for x in a if x not in b]

# 9
def stringMatching(words):
    result = []
    for word in words:
        for i in words:
            if word in i and word != i:
                result.append(word)
                break
    return result

# 10
def oddnumber(num):
    i = len(num) - 1
    while i >= 0:
        if int(num[i])%2 != 0:
            return num[:i+1]
        i -= 1
    return ''

# 11
def twoSum(nums, target):
    for i in range(len(nums) - 1): # el -1 es para optimizar y que no itere una vez mas al pedo
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# 12

def checkRecord(s: str) -> bool:
    a_count = 0
    l_count = 0
    for i in s:
        if i == 'A':
            a_count += 1
            l_count = 0
        elif i == 'L':
            l_count += 1
            if l_count > 2:
                return False
        else:
            l_count = 0
        if a_count > 1:
            return False
    return True

# alt

def checkRecord_alt(s):
    if s.find("LLL") >= 0:
        return False

    if s.count("A") > 1:
        return False

    return True

# alt2

def checkRecord_alt2(s):
    return "LLL" not in s and s.count("A") <= 1

# 13

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

# 14

def romanToInt(s: str) -> int:
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    ans = 0
    for i in range(len(s)):
        if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
            ans -= d[s[i]]
        else:
            ans += d[s[i]]
    
    return ans

# 15

def mergeTwoLists(list1, list2):
    for k in list2:
        list1.append(k)
    list1.sort()
    return list1

# 16 (Pointers)

def threeSum(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1

                while nums[j] == nums[j-1] and j < k:
                    j += 1
    
    return res

# 17

def majorityElement(nums):
    d = {}
    ans = None
    count = 0
    for x in nums:
        if x in d:
            d[x] +=1
        else:
            d[x] = 1
    for x, y in d.items():
        if y > count:
            count = y
            ans = x
    return ans