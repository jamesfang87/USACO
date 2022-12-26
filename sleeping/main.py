from functools import reduce
from math import sqrt


num_problems = int(input().strip('\n'))

problems = []

for i in range(num_problems):
    num_days = int(input().strip('\n'))
    values = input().strip('\n').split(' ')
    problems.append([int(item) for item in values])


def find_answer(numbers):
    sum_list = sum(numbers)
    return factors(sum_list)


def factors(n):
    if n != 0:
        step = 2 if n % 2 else 1
        return set(reduce(list.__add__,
                          ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))


for problem in problems:

    if len(set(problem)) == 1:
        print(0)
        continue
    found_factors = list(find_answer(problem))
    sum_in_problem = sum(problem)

    if len(found_factors) == 2:
        print(len(problem) - found_factors[0])

    else:
        found_factors.sort()
        for number in reversed(found_factors):
            max_sum_in_each = sum_in_problem / number
            sum_in_section = 0
            count_successful = 0
            break_out = False
            done = False

            for num_hour in problem:
                sum_in_section += num_hour
                if sum_in_section > max_sum_in_each:
                    sum_in_section = 0
                    break_out = True
                    break
                elif sum_in_section == max_sum_in_each:
                    count_successful += 1
                    sum_in_section = 0

                if count_successful == number:
                    print(len(problem) - number)
                    done = True

            if break_out:
                continue

            if done:
                break
