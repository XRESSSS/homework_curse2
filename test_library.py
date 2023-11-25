
from library import cm_to_inches


def test_first_cm_to_inches():
    length_in_cm_1 = 30
    result_1 = cm_to_inches(length_in_cm_1)
    assert result_1 == 11.81


def test_second_cm_to_inches():
    length_in_cm_2 = 0.03
    result_2 = cm_to_inches(length_in_cm_2)
    assert result_2 == 0.01


def test_third_cm_to_inches():
    length_in_cm_3 = -25
    result_3 = cm_to_inches(length_in_cm_3)
    assert result_3 == 25


def test_fourth_cm_to_inches():
    length_in_cm_4 = 1000
    result_4 = cm_to_inches(length_in_cm_4)
    assert result_4 == 393.7
