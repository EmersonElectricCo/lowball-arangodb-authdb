
"""According to https://github.com/ArangoDB-Community/pyArango/blob/dev/README.rst

Validators must Inherit Validator and implement a validate function
which returns True or raises a Validation Error

"""
import pytest
from pyArango.validation import ValidationError
from lowball_arangodb_authdb.token_validators import TokenIDValidator
from lowball.models.authentication_models.token import TOKEN_ID_PATTERN
import re

class TestTokenIDValidator:

    def test_validate_raises_validation_error_for_invalid_token_ids_that_dont_match_token_regex(self, invalid_token_ids,
                                                                                                wrapped_re_fullmatch):
        validator = TokenIDValidator()
        with pytest.raises(ValidationError):
            validator.validate(invalid_token_ids)

        re.fullmatch.assert_called_once_with(TOKEN_ID_PATTERN, invalid_token_ids)

    def test_validate_returns_true_for_valid_token_ids(self, valid_token_ids, wrapped_re_fullmatch):
        validator = TokenIDValidator()

        assert validator.validate(valid_token_ids) == True
        re.fullmatch.assert_called_once_with(TOKEN_ID_PATTERN, valid_token_ids)


class TestClientIDValidator:

    def test_raises_validation_error_for_invalid_client_ids(self):

        pass


class TestRolesValidator:

    pass


class TestTimestampValidator:

    pass


