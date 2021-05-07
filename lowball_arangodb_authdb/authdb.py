from lowball.models.authentication_models import Token, valid_token_id
from lowball.models.provider_models import AuthDatabase


class AuthDB(AuthDatabase):

    def __init__(self):

        AuthDatabase.__init__(self)

    def add_token(self, token_object):

        pass

    def lookup_token(self, token_id):

        pass

    def revoke_token(self, token_id):

        pass

    def revoke_all(self):

        pass

    def list_tokens(self):

        pass

    def list_tokens_by_client_id(self, client_id):

        pass

    def list_tokens_by_role(self, role):

        pass

    def cleanup_tokens(self):

        pass