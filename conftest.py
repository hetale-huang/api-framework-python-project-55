import pytest

from utils.file_reader import read_file


@pytest.fixture(scope="session")
def context():
    return {}


@pytest.fixture(scope="session")
def create_data():
    yield read_file("tests/data/create_booking.json")


@pytest.fixture(scope="session")
def update_data():
    yield read_file("tests/data/update_booking.json")
