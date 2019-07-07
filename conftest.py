# conftest.py
from unittest import mock
import pytest
import connexion
import library


@pytest.fixture(scope='session')
def setup_mocked_search():
    """Sets up spy fr search function."""
    with mock.patch.object(library.employee, 'search', wraps=library.employee.search) as mock_search:
        yield mock_search


@pytest.fixture(scope='function')
def mocked_search(setup_mocked_search):
    """Resets search spy."""
    setup_mocked_search.reset_mock()
    return setup_mocked_search


@pytest.fixture(scope='session')
def app(setup_mocked_search):
    """Flask app for testing."""
    # Adding swagger file
    test_app = connexion.FlaskApp(__name__, specification_dir='.')
    test_app.add_api('specification.yml')

    return test_app.app
