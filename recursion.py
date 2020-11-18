from typing import List
import sys

BASE_NUMBERS: List = [1, 3, 4]

def main():
    if len(sys.argv) == 2:
        try:
            parameter = int(sys.argv[1])

            calculate_sum(parameter)
            return
        except ValueError:
            pass
    
    print('Wrong parameter')


def calculate_sum(target_sum: int, numbers: List[int] = []) -> List[int]:
    """
    Calculates all sum combinations using recursion.
    """
    try:
        t_sum = sum(numbers)
    except TypeError:
        t_sum = 0
    
    if t_sum == target_sum:
        print(numbers)
    elif t_sum < target_sum:
        for i in BASE_NUMBERS:
            calculate_sum(target_sum, numbers + [i])


if __name__ == "__main__":
    main()