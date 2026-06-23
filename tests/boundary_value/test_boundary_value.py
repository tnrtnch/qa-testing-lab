def is_valid_password(password):
    return len(password) >= 8


def test_password_boundary_values():

    # Boundary - 1
    assert is_valid_password("1234567") is False

    # Boundary
    assert is_valid_password("12345678") is True

    # Boundary + 1
    assert is_valid_password("123456789") is True