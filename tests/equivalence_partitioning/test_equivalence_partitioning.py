def is_valid_age(age):
    return 18 <= age <= 65


def test_age_equivalence_partitioning():

    # Invalid partition (<18)
    assert is_valid_age(10) is False

    # Valid partition (18-65)
    assert is_valid_age(30) is True

    # Invalid partition (>65)
    assert is_valid_age(70) is False