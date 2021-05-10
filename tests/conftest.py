import pytest
from unittest.mock import Mock, MagicMock
from datetime import datetime
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

