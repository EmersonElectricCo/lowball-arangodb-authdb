from pyArango.validation import Validator, ValidationError
from lowball.models.authentication_models.token import TOKEN_ID_PATTERN
import re

class TokenIDValidator(Validator):
    """Simple Validator to make sure the token id
    is checked against lowball's token id format

    """
    def validate(self, value):

        try:
            result = re.fullmatch(TOKEN_ID_PATTERN, value)
        except:
            result = None
        if not result:
            raise ValidationError(f"Token ID Must match {TOKEN_ID_PATTERN}")
        return True


class ClientIDValidator(Validator):
    """Simple validator to make sure the
    client id and requesting client id are
    valid strings

    """
    def validate(self, value):
        pass


class TimestampValidator(Validator):
    """simple validator to ensure that the
    creation and expiration timestamps are in
    the correct format

    """
    def validate(self, value):
        pass


class RolesValidator(Validator):
    """simple validator to ensure that the
    roles field is a list of strings

    """
    def validate(self, value):

        pass

