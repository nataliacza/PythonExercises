from challenges.task_001 import is_nested_3, is_nested_4
from challenges.task_002 import is_all_equal
from challenges.task_003 import is_valid_array
from challenges.task_004 import swap_elements


if __name__ == '__main__':

    # TASK 001
    is_nested_3([])
    is_nested_3([[2, 3], [5, 5]])
    is_nested_3([[1, 2], 4])
    is_nested_3([[1, 2], (0,)])

    is_nested_4([])  # False
    is_nested_4([[2, 3], [5, 5]])  # True
    is_nested_4([[1, 2], 4])  # False
    is_nested_4([[1, 2], (0,)])  # False
    is_nested_4([[1, 2], (0,), [5, 5], [5, 5, 5]])  # False

    # TASK 002
    is_all_equal([4, 5, 6])
    is_all_equal([4, 4, 4])
    is_all_equal([4, 4, "4"])

    # TASK 003
    is_valid_array([[3], [4]])
    is_valid_array([[3, 4], [4, 5]])
    is_valid_array([[3, 4, 5], [4, 5]])

    # TASK 004
    swap_elements([4, 5, 6, 7])  # [7, 5, 6, 4]
    swap_elements([4, 5, 6, 7, 1])  # [1, 5, 6, 7, 4]
    swap_elements([4, 5])  # [5, 4]
    swap_elements([])  # []
