import pytest
from unittest.mock import Mock, MagicMock
from datetime import datetime
import pathlib
import re

@pytest.fixture(params=[
    "right_length_bad",
    "wronglength",
    "wrongerlengthtoolong",
    ["not", "a", "string"],
    "",
    None,
    {},
    1,
    3,
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"],
    "AGoodTryButNope!"
])
def invalid_token_ids(request):

    return request.param

@pytest.fixture(params=[
    "abcdEFGH13578642",
    "zx73hg5490ljHGHF",
    "asimpletokenidya",
    "4Simpl3T0ken1dyA"
])
def valid_token_ids(request):

    return request.param

@pytest.fixture
def wrapped_re_fullmatch(monkeypatch):

    monkeypatch.setattr(re, "fullmatch", Mock(wraps=re.fullmatch))

@pytest.fixture(params=[
    "short_client_id",
    "different cleint id",
    "CLINET_DI"
])
def nonemptystrings(request):
    return request.param


@pytest.fixture(params=[
    [],
    ["r1", "r2", "r3"],
    ["r1"]
])
def valid_roles(request):
    return request.param


@pytest.fixture(params=[
    "2020-05-10 10:20:30",
    "1991-05-02 16:30:00",
    "2030-12-31 00:00:00"
])
def valid_datetimes(request):

    return request.param



@pytest.fixture(params=[
    "not even close",
    "2020:10:4T00:00:00",
    "2020-13-4 00:00:00",
    "2020-11-4 25:00:00"
])
def invalid_datetimes(request):

    return request.param

@pytest.fixture(
    params=[
        ["not", "string"],
        1234,
        "string.but.missing.specifier",
        "",
        None

    ]
)
def invalid_urls(request):
    return request.param

@pytest.fixture(params=[
    "http://127.0.0.1",
    "https://127.0.0.1",
    "https://any.string"
])
def valid_urls(request):

    return request.param

@pytest.fixture(params=[
    "not integer",
    "40",
    0,
    70000,
    65536,
    7.2,
    None
])
def invalid_ports(request):

    return request.param

@pytest.fixture(params=[
    80,
    443,
    8529,
    8443,
    8080,
    1,
    65535
])
def valid_ports(request):
    return request.param

@pytest.fixture(params=[
    "",
    ["not", "a", "string"],
    None
])
def not_strings_or_empty(request):
    return request.param


@pytest.fixture(params=[
    ["not", "string"],
    1234
])
def just_not_string(request):
    return request.param

@pytest.fixture(params=[
    "",
    "12345",
    None
])
def string_or_none(request):
    return request.param

@pytest.fixture(params=[
    50,
    "not string path",
    ["not", "bool"]
])
def not_bool_or_string_path(request):
    return request.param

@pytest.fixture(params=[
    "/path/to/file.ca",
    "/another/path",
    True,
    False
])
def valid_verify(request, path_does_exist, path_is_file):
    return request.param

@pytest.fixture
def path_does_not_exist(monkeypatch):

    monkeypatch.setattr(pathlib.Path, "exists", Mock(return_value=False))

@pytest.fixture
def path_does_exist(monkeypatch):
    monkeypatch.setattr(pathlib.Path, "exists", Mock(return_value=True))

@pytest.fixture
def path_is_file(monkeypatch):
    monkeypatch.setattr(pathlib.Path, "is_file", Mock(return_value=True))

@pytest.fixture
def path_is_not_file(monkeypatch):
    monkeypatch.setattr(pathlib.Path, "is_file", Mock(return_value=False))

@pytest.fixture(params=[
    "_system",
    "",
    None,
    ["not", "string"],
    1
])
def invalid_database_name(request):
    return request.param

@pytest.fixture(params=[
    "Collection",
    "SystemCollection",
    "Edges",
    "",
    None,
    ["not", "string"],
    1
])
def invalid_collection_name(request):
    return request.param
