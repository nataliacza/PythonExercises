from task_001 import is_nested, is_nested_2, is_nested_3, is_nested_4
from task_002 import is_all_equal, is_all_equal_2
from task_003 import is_valid_array

if __name__ == '__main__':

    # TAKS 001
    is_nested_3([])
    is_nested_3([[2, 3], [5, 5]])
    is_nested_3([[1, 2], 4])
    is_nested_3([[1, 2], (0,)])

    is_nested_4([])  # False
    is_nested_4([[2, 3], [5, 5]])  # True
    is_nested_4([[1, 2], 4])  # False
    is_nested_4([[1, 2], (0,)])  # False
    is_nested_4([[1, 2], (0,), [5, 5], [5, 5, 5]])  # False

    # TAKS 002
    is_all_equal([4, 5, 6])
    is_all_equal([4, 4, 4])
    is_all_equal([4, 4, "4"])

    # TAKS 003
    is_valid_array([[3], [4]])
    is_valid_array([[3, 4], [4, 5]])
    is_valid_array([[3, 4, 5], [4, 5]])
