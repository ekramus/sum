from typing import List
import sys

BASE_NUMBERS: List = [4, 3, 1]

def main():
    if len(sys.argv) == 2:
        try:
            parameter = int(sys.argv[1])

            calculate_sum(parameter)
            return
        except ValueError:
            pass
    
    print('Wrong parameter')


def calculate_sum(target_sum: int, numbers: List[int] = []):
    """
    Calculate all sum combinations using just iteration.
    """
    # create leaf stack and add initial leafs to the stack
    leaf_stack: List[List] = []
    leaf_stack.append(list(BASE_NUMBERS))

    current_sum: int = 0

    # while there are leafs in leaf stack
    while leaf_stack:
        # retrieve leaf from the stack
        leafs: List = leaf_stack[-1]
        new_leaf = leafs.pop()
        numbers = numbers + [new_leaf]
        current_sum += new_leaf
        
        # print numbers if sum matches target sum
        if current_sum == target_sum:
            print(numbers)
        # if less than target sum, add new leafs level
        elif current_sum < target_sum:
            leaf_stack.append(list(BASE_NUMBERS))

        # is sum is greater or equal to target sum, remove last item from numbers list and decrease current sum
        if current_sum >= target_sum:
            removed_leaf = numbers.pop()
            current_sum -= removed_leaf
        
        # remove all empty records in leaf_stack and backtrack numbers list
        leafs = leaf_stack[-1]
        while not leafs:
            # remove empty top leafs from leaf stack
            leaf_stack.pop()
            # get current top leafs (if leaf_stack not empty)
            try:
                leafs = leaf_stack[-1]
            except IndexError:
                break
            # remove last leaf from numbers and decrease current sum
            removed_leaf = numbers.pop()
            current_sum -= removed_leaf

    pass

if __name__ == "__main__":
    main()