
class TestAuthDBInit:
    """Tests:

    initialization with connection object,
    initial database setup if it doesnt exist
    defaults for everything

    Parameters:
        arango_url="http://127.0.0.1"
        arango_port=8529
        user="root"
        password=None
        verify=True
        database_name="lowball"
        collection_name="authentication_tokens"
        index_client_id=True

    arango_url should include http:// or https://

    arango_port should be valid integer

    user: string
    password: string

    verify: boolean OR string -> path to ca

    database_name: string

    collection_name: string

    index_client_id: bool

    _key = token id

    I think we can keep this implementation low level

    index client id would allow faster lookups by client id for tokens
    The collection will be used to hold token documents, organized by tokenid

    Should setup Validators for the token documents in the collection

    Alright, validators are interesting. So we set them in a Collection class
    definition. It seems that when we db.createCollection

    Document objects??? I don't think so, should be able to translate back
    and forth between a doc and a Token object with ease

    looks like we should be able to leverage their metaclass setup by using this

    Collection_metaclass.collectionClasses["desired_collection_name"] = OurClass
    Looks like to preserve structure we need to restrict their names from Collection, SystemCollection, and Edges,
    but anything else is fair game
    """
    def test_init_accepts_expected_kwargs(self):

        pass

    def test_validation_of_arango_url_parameter(self):

        pass

    def test_validation_of_arango_port_parameter(self):

        pass

    def test_validation_of_arango_user_parameter(self):

        pass

    def test_validation_of_arango_password_parameter(self):

        pass

    def test_validation_of_verify_parameter(self):

        pass

    def test_validation_of_database_name_parameter(self):
        pass

    def test_validation_of_collection_name_parameter(self):

        pass

    def test_validation_of_index_client_id_parameter(self):

        pass

    def test_arango_connection_created_correctly(self):

        pass

    def test_failure_cases_for_arango_connection(self):

        pass

    def test_authentication_database_created_if_not_present(self):

        pass

    def test_authentication_database_accessed_if_present(self):

        pass

    def test_authentication_collection_created_if_not_present(self):

        pass

    def test_authentication_collection_accessed_if_present(self):
        pass

    def test_client_id_index_created_if_set_to_true(self):
        pass

    def test_client_id_index_removed_if_set_to_false(self):

        pass


class TestAddToken:

    pass


class TestLookupToken:

    pass


class TestRevokeToken:

    pass


class TestRevokeAll:

    pass


class TestListTokens:

    pass


class TestListTokensByClientID:

    pass


class TestListTokensByRole:

    pass


class TestCleanupTokens:

    pass