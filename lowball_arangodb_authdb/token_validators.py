from pyArango.validation import Validator, ValidationError


class TokenIDValidator(Validator):
    """Simple Validator to make sure the token id
    is checked against lowball's token id format

    """
    def validate(self, value):

        pass


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

