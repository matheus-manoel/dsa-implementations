def ugly_numbers():
    ugly_numbers = [1]
    initial_numbers = [2, 3, 5]
    positions_and_numbers = [[0, 2], [0, 3], [0, 5]]

    for _ in range(100):
        minimum = float('inf')
        minimum_position = float('inf')
        for i, p_n in enumerate(positions_and_numbers):
            if p_n[1] < minimum:
                minimum = p_n[1]
                minimum_position = i

        if ugly_numbers[-1] != minimum:
            ugly_numbers.append(minimum)

        positions_and_numbers[minimum_position][0] += 1
        positions_and_numbers[minimum_position][1] = initial_numbers[minimum_position] * positions_and_numbers[minimum_position][0]

    print(ugly_numbers)

ugly_numbers()
