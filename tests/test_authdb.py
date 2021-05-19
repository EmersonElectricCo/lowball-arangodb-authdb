import pytest

from lowball_arangodb_authdb.authdb import AuthDB, AuthenticationCollection
from unittest.mock import call
import pyArango
from pyArango.connection import Connection
from pyArango.collection import Collection, Collection_metaclass
from pyArango.database import Database
from pyArango.document import Document

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

    arango_url should include http:// or https://, i think we rely on the connection class to validate any further here

    arango_port should be valid integer

    user: string (non empty)
    password: string/none

    verify: boolean OR string -> path to ca

    database_name: string

    collection_name: string


    _key = token id

    I think we can keep this implementation low level meaning, not creating high level of abstraction. Tokens should
    be immutable once created

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

    def test_init_sets_expected_defaults(self, basic_mock_pyarango, mock_pyarango):

        authdb = AuthDB()

        assert authdb.url == "http://127.0.0.1"
        assert authdb.port == 8529
        assert authdb.user == "root"
        assert authdb.password == None
        assert authdb.verify == True
        assert authdb.database_name == "lowball_authdb"
        assert authdb.collection_name == "authentication_tokens"

    def test_init_accepts_expected_kwargs(self, basic_mock_pyarango, mock_pyarango):

        authdb = AuthDB(
            url="https://local.arango",
            port=8080,
            user="lowball",
            password="supersafe",
            verify=False,
            database_name="authdb",
            collection_name="token_store",
        )

        assert authdb.url == "https://local.arango"
        assert authdb.port == 8080
        assert authdb.user == "lowball"
        assert authdb.password == "supersafe"
        assert authdb.verify == False
        assert authdb.database_name == "authdb"
        assert authdb.collection_name == "token_store"

    # test validation of arango url parameter beyond making sure it's a string with http/https in front
    def test_arango_url_error_if_not_string_or_missing_http_specifier(self,
                                                                      invalid_urls,
                                                                      mock_pyarango,
                                                                      basic_mock_pyarango):

        with pytest.raises(ValueError):
            AuthDB(url=invalid_urls)

    def test_arango_url_no_error_if_set_correctly(self,
                                                  valid_urls,
                                                  mock_pyarango,
                                                  basic_mock_pyarango):
        authdb = AuthDB(url=valid_urls)
        assert authdb.url == valid_urls

    def test_validation_of_arango_port_parameter_as_integer_as_valid_port_number(self,
                                                                                 invalid_ports,
                                                                                 mock_pyarango,
                                                                                 basic_mock_pyarango):
        with pytest.raises(ValueError):
            AuthDB(port=invalid_ports)

    def test_arango_port_no_error_when_correct_ports(self,
                                                     valid_ports,
                                                     mock_pyarango,
                                                     basic_mock_pyarango):
        authdb = AuthDB(port=valid_ports)
        assert authdb.port == valid_ports

    def test_validation_of_arango_user_parameter_nonempty_string(self,
                                                                 not_strings_or_empty,
                                                                 mock_pyarango,
                                                                 basic_mock_pyarango):
        with pytest.raises(ValueError):
            AuthDB(user=not_strings_or_empty)

    def test_arango_user_no_error_when_nonempty_string(self,
                                                       nonemptystrings,
                                                       mock_pyarango,
                                                       basic_mock_pyarango):
        authdb = AuthDB(user=nonemptystrings)
        assert authdb.user == nonemptystrings

    def test_validation_of_arango_password_parameter_is_string_or_none(self,
                                                                       just_not_string,
                                                                       mock_pyarango,
                                                                       basic_mock_pyarango):
        with pytest.raises(ValueError):
            AuthDB(password=just_not_string)

    def test_arango_password_no_error_when_string_or_none(self,
                                                          string_or_none,
                                                          mock_pyarango,
                                                          basic_mock_pyarango):
        authdb = AuthDB(password=string_or_none)
        assert authdb.password == string_or_none

    def test_validation_of_verify_parameter_when_not_bool_or_string_path_file(self,
                                                                              not_bool_or_string_path,
                                                                              mock_pyarango,
                                                                              basic_mock_pyarango):
        with pytest.raises(ValueError):
            AuthDB(verify=not_bool_or_string_path)

    def test_validation_of_verify_parameter_when_path_does_not_exist(self,
                                                                     path_does_not_exist,
                                                                     mock_pyarango,
                                                                     basic_mock_pyarango):

        with pytest.raises(ValueError):
            AuthDB(verify="/non_existent/path")

    def test_validation_of_verify_parameter_when_path_does_exist_but_is_not_a_file(self,
                                                                                   path_does_exist,
                                                                                   path_is_not_file,
                                                                                   mock_pyarango,
                                                                                   basic_mock_pyarango):
        with pytest.raises(ValueError):
            AuthDB(verify="/non_existent/file_path")

    def test_verify_no_error_when_bool_or_string_path_that_exists(self,
                                                                  valid_verify,
                                                                  mock_pyarango,
                                                                  basic_mock_pyarango):

        authdb = AuthDB(verify=valid_verify)
        assert authdb.verify == valid_verify

    def test_validation_of_database_name_parameter_if_not_string_or_system_db(self,
                                                                              invalid_database_name,
                                                                              mock_pyarango,
                                                                              basic_mock_pyarango):
        with pytest.raises(ValueError):
            AuthDB(database_name=invalid_database_name)

    def test_database_name_when_string_but_not_system(self,
                                                      nonemptystrings,
                                                      mock_pyarango,
                                                      basic_mock_pyarango):
        authdb = AuthDB(database_name=nonemptystrings)
        assert authdb.database_name == nonemptystrings

    def test_validation_of_collection_name_parameter_if_not_string_or_reserved_name(self,
                                                                                    invalid_collection_name,
                                                                                    mock_pyarango,
                                                                                    basic_mock_pyarango):
        with pytest.raises(ValueError):
            AuthDB(collection_name=invalid_collection_name)

    def test_collection_name_when_string_but_not_reserved(self,
                                                          mock_pyarango,
                                                          nonemptystrings,
                                                          basic_mock_pyarango):
        authdb = AuthDB(collection_name=nonemptystrings)
        assert authdb.collection_name == nonemptystrings

    def test_arango_connection_created_correctly(self, mock_pyarango, init_calls_expected_connection,
                                                 basic_mock_pyarango,
                                                 basic_mock_connection):

        params, expected_call = init_calls_expected_connection

        auth_db = AuthDB(*params)

        auth_db.connection.__init__.assert_has_calls([expected_call])

    def test_authentication_database_created_if_not_present(self,
                                                            mock_pyarango,
                                                            basic_mock_connection_get_item_db_not_present,
                                                            mock_init_collection,
                                                            basic_db_name):

        authdb = AuthDB(database_name=basic_db_name)
        authdb.connection.__getitem__.assert_called_once_with(basic_db_name)
        authdb.connection.createDatabase.assert_called_once_with(name=basic_db_name)

        assert isinstance(authdb.database, Database)
        assert authdb.database.name == basic_db_name

    def test_authentication_database_accessed_if_present(self,
                                                         mock_pyarango,
                                                         basic_db_name,
                                                         mock_init_collection,
                                                         mock_connection_get_item_db_present):
        authdb = AuthDB(database_name=basic_db_name)
        authdb.connection.__getitem__.assert_called_once_with(basic_db_name)

        assert isinstance(authdb.database, Database)
        assert authdb.database.name == basic_db_name


    def test_named_authentication_collection_is_correctly_set(self,
                                                              mock_pyarango,
                                                              basic_db_name,
                                                              mock_connection_get_item_db_present,
                                                              mock_init_database,
                                                              mock_init_collection,
                                                              nonemptystrings
                                                              ):
        authdb = AuthDB(collection_name=nonemptystrings)

        assert Collection_metaclass.collectionClasses.get(nonemptystrings) == AuthenticationCollection


    def test_authentication_collection_created_if_not_present(self,
                                                              mock_pyarango,
                                                              mock_database_getitem_collection_not_present,
                                                              nonemptystrings
                                                              ):
        authdb = AuthDB(collection_name=nonemptystrings)

        authdb.database.__getitem__.assert_called_once_with(nonemptystrings)
        authdb.database.createCollection.assert_called_once_with(authdb.collection_name, waitForSync=True)
        assert isinstance(authdb.collection, AuthenticationCollection)

    def test_authentication_collection_accessed_if_present(self,
                                                           mock_pyarango,
                                                           mock_database_getitem_collection_present,
                                                           nonemptystrings):

        authdb = AuthDB(collection_name=nonemptystrings)

        authdb.database.__getitem__.assert_called_once_with(nonemptystrings)
        assert isinstance(authdb.collection, AuthenticationCollection)


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


class TestAuthenticationCollection:
    """The authentication collecion will be a collection class that has the validators
    instantiated properly so as to

    """
    pass