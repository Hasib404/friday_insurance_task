import pytest
from fastapi.testclient import TestClient

from api.address.controller import AddressParser
from main import app
from schemas.address import AddressRequestModel


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_address_contains_less_than_2_words(client):
    address = AddressRequestModel(address="123")
    response = client.post("/address/", json=address.dict())
    assert response.status_code == 400
    assert response.json() == {"detail": "Address should contain at least 2 words"}


def test_address_does_not_contain_any_digits(client):
    address = AddressRequestModel(address="Main St.")
    response = client.post("/address/", json=address.dict())
    assert response.status_code == 400
    assert response.json() == {"detail": "Address should contain at least one digit"}


def test_address_does_not_contain_any_alphabetic_characters(client):
    address = AddressRequestModel(address="1234 5577")
    response = client.post("/address/", json=address.dict())
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Address should contain some alphabetic characters"
    }


def test_parse_valid_address():
    parser = AddressParser()
    result = parser.parse_address("Winterallee 3")
    assert result == {"street": "Winterallee", "housenumber": "3"}


def test_parse_address_one_word_street():
    parser = AddressParser()
    result = parser.parse_address("Blaufeldweg 123B")
    assert result == {"street": "Blaufeldweg", "housenumber": "123B"}


def test_parse_address_two_word_street():
    parser = AddressParser()
    result = parser.parse_address("Am Bächle 23")
    assert result == {"street": "Am Bächle", "housenumber": "23"}


def test_parse_address_multiple_word_street():
    parser = AddressParser()
    result = parser.parse_address("Auf der Vogelwiese 23 b")
    assert result == {"street": "Auf der Vogelwiese", "housenumber": "23 b"}


def test_parse_address_with_housenumber_at_start_with_comma():
    address = "4, rue de la revolution"
    expected_result = {"street": "rue de la revolution", "housenumber": "4"}
    parser = AddressParser()
    result = parser.parse_address(address)
    assert result == expected_result


def test_parse_address_with_housenumber_at_end_with_comma():
    address = "Calle Aduana, 29"
    expected_result = {"street": "Calle Aduana", "housenumber": "29"}
    parser = AddressParser()
    result = parser.parse_address(address)
    assert result == expected_result


def test_parse_address_with_street_with_digits():
    address = "Calle 39 No 1540"
    expected_result = {"street": "Calle 39", "housenumber": "No 1540"}
    parser = AddressParser()
    result = parser.parse_address(address)
    assert result == expected_result
