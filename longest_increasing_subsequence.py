def auxLis(v, index, memo=None):
    if memo is None:
        memo = [None] * len(v)

    if memo[index]:
        return memo[index]

    ret = 1
    for i in range(index+1, len(v)):
        if v[i] > v[index]:
            ret = max(ret, auxLis(v, i, memo) + 1)


    memo[index] = ret

    return ret


def longest_increasing_subsequence(v):
    ret = auxLis(v, 0)
    for i in range(1, len(v)):
        ret = max(ret, auxLis(v, i))
    return ret


print(longest_increasing_subsequence([0, 109, 4, 6, -1, 5, 6, 7, 3, 7, 8]))


# Da Manu:


def auxLis(v, index, cache):
    ret = 1
    for i in range(index+1, len(v)):
        if v[i] > v[index]:
            ret = max(ret, cache[i]+1)
    cache[index] = ret
    return ret


def lis(v):
    n = len(v)
    cache = [None]*n
    ret = auxLis(v, n-1, cache)
    for i in range(n-2, -1, -1):
        ret = max(ret, auxLis(v, i, cache))
    return ret


# Do prof


def lisProf(v):
    memo = [None] * len(v)
    memo[len(v) - 1] = 1
    for i in range(len(v) - 2, -1, -1):
        res = 1
        for j in range(i+1, len(v)):
            if v[j] > v[i]:
                res = max(res, memo[j] + 1)
        memo[i] = res
    return max(memo)


# Da internet

def lis(nums):
  dp = [1] * len(nums)
  for i in range(1, len(nums)):
      for j in range(i):
          if nums[i] > nums[j]:
              dp[i] = max(dp[i], dp[j] + 1)

  return max(dp)
