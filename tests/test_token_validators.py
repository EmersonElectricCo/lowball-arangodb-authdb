
"""According to https://github.com/ArangoDB-Community/pyArango/blob/dev/README.rst

Validators must Inherit Validator and implement a validate function
which returns True or raises a Validation Error

"""


class TestTokenIDValidator:

    def test_validate_raises_validation_error_for_invalid_token_ids(self):

        pass

    def test_validate_returns_true_for_valid_token_ids(self):

        pass


class TestClientIDValidator:

    def test_raises_validation_error_for_invalid_client_ids(self):

        pass


class TestRolesValidator:

    pass


class TestTimestampValidator:

    pass


