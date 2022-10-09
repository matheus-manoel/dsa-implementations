def longest_commom_sequence(s1, s2, index_1, index_2, cache=None):
    if cache is None:
        cache = {}

    if (index_1, index_2) in cache:
        return cache[(index_1, index_2)]

    if index_1 == -1 or index_2 == -1:
        return 0

    if s1[index_1] == s2[index_2]:
        cache[(index_1, index_2)] = longest_commom_sequence(
                s1, s2, index_1 - 1, index_2 - 1, cache
        ) + 1
    else:
        cache[(index_1, index_2)] = max(
            longest_commom_sequence(s1, s2, index_1 - 1, index_2, cache),
            longest_commom_sequence(s1, s2, index_1, index_2 - 1, cache)
        )

    return cache[(index_1, index_2)]
