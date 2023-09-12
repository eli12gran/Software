from models import *
import numpy.testing as npt
import numpy as np

test_input = np.array([[1,2],[3,4],[5,6]])
test_result = np.array([3,4])
npt.assert_array_equal(daily_mean(test_input), test_result)


test_result_max = np.array([[2], [4], [6]])
npt.assert_array_equal(daily_max(test_input), test_result_max)

test_result_min = np.array([[1],[3],[5]])
npt.assert_array_equal(daily_min(test_input), test_result_min)