"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest
from inflammation.models import daily_mean, daily_min, daily_max, patient_normalise


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


# def test_daily_mean_integers():
# """Test that mean function works for an array of positive integers."""
# from inflammation.models import daily_mean

# test_input = np.array([[1, 2],
#                     [3, 4],
#                    [5, 6]])
# test_result = np.array([3, 4])

# Need to use Numpy testing functions to compare arrays
# npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_max():
    """Test that mean functions works for an array of positive integers"""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([5, 6])

    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_min():
    """Test that mean functions works for an array of positive integers"""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([1, 2])

    npt.assert_array_equal(daily_min(test_input), test_result)


'''
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers"""
    npt.assert_array_equal(daily_mean(test), expected)
'''


@pytest.mark.parametrize(
    "test, expected",
    [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]])

     ])
def test_patient_normalise(test, expected):
    """Test normalisation works for arrays of one and positive integers,
    Assumption that test accuracy of two decimal places is sufficient"""
    npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
