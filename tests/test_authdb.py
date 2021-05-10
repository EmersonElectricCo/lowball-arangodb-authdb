
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

    arango_url should include http:// or https://, i think we rely on the connection class to validate any further here

    arango_port should be valid integer

    user: string (non empty)
    password: string/none

    verify: boolean OR string -> path to ca

    database_name: string

    collection_name: string

    index_client_id: bool

    _key = token id

    I think we can keep this implementation low level meaning, not creating high level of abstraction. Tokens should
    be immutable once created

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

    def test_error_when_not_given_token_object(self):

        pass

    def test_failure_when_token_already_exists(self):

        pass

    def test_add_token_calls_create_document_with_token_dictionary(self):

        pass

    def test_add_token_sets_new_document_key_to_token_id_and_saves(self):

        pass


class TestLookupToken:

    def test_returns_none_when_token_not_found(self):

        pass

    def test_deletes_token_if_token_information_cannot_be_loaded_into_token_when_found(self):
        pass

    def test_returns_token_object_when_token_document_found(self):

        pass


class TestRevokeToken:

    def test_returns_none_when_token_not_found(self):
        pass

    def test_calls_delete_on_token_document_when_found(self):
        pass


class TestRevokeAll:

    def test_calls_delete_on_each_document_in_the_database(self):

        pass


class TestListTokens:

    def test_returns_list_of_token_objects(self):

        pass

    def test_returns_all_documents_in_the_database_as_token_objects(self):

        pass



class TestListTokensByClientID:
    """Should expect an aql query here.
    We will probably build a constructor utility function to build it properly

    I know we want to parameterize the query

    """

    def test_returns_list_of_token_objects(self):
        pass

    def test_all_tokens_in_list_are_owned_by_the_specified_client_id(self):
        """Not sure we can test this properly, as the actual filtering is done on the arango side

        all we can test is calling the query correctly

        """
        pass

    def test_aql_query_called_with_correct_inputs(self):

        pass


class TestListTokensByRole:
    """This may be an aql queryable option as well, will hae to investigate

    """
    def test_returns_list_of_token_objects(self):
        pass

    def test_all_tokens_in_list_possess_the_requested_role(self):

        pass

    def test_aql_query_called_with_correct_inputs(self):
        pass


class TestCleanupTokens:
    """i believe this is again an aql query we can do

    """
    def test_calls_delete_on_all_tokens_which_are_expired(self):

        pass

    def test_aql_query_called_with_correct_inputs(self):

        pass