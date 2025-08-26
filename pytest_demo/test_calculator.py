# import pytest
from calculator import add, divide

# def test_add_correct():
#   assert add(2, 3) == 5 # kiểm tra logic cộng đúng
# def test_divide_normal():
#   assert divide(10, 2) == 5 # kiểm tra chia bình thường

# def test_divide_by_zero():
#   with pytest.raises(ZeroDivisionError):
#     divide(10, 0) # kiểm tra chia cho 0 ném ra exception



# import pytest
# @pytest.fixture

# def sample_list():
#   return [1, 2, 3]

# def test_sum_list(sample_list):
#   assert sum(sample_list) == 6



import pytest

@pytest.mark.parametrize("a,b,expected", [
  (1, 2, 3),
  (0, 0, 0),
  (-1,-1,-2),
])

def test_add_multiple(a, b, expected):
  assert add(a, b) == expected