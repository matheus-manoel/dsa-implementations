v = [
  [6008, 1300],
  [6000, 2100],
  [500, 2000],
  [1000, 4000],
  [1100, 3000],
  [6000, 2000],
  [8000, 1400],
  [6000, 1200],
  [2000, 1900]
]


def maiorSeqComecandoEm(v, index, memo):
    if memo[index]:
        return memo[index]

    ret = 1
    for i in range(len(v)):
        if v[i][0] > v[index][0] and v[i][1] < v[index][1]:
            aux = maiorSeqComecandoEm(v, i, memo) + 1
            ret = max(ret, aux)

    memo[index] = ret
    return ret


def maiorSeq(v):
    ret = 0
    memo = [None] * len(v)
    for i in range(len(v)):
        aux = maiorSeqComecandoEm(v, i, memo)
        ret = max(ret, aux)
    return ret


print(maiorSeq(v))
