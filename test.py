# test.py
"""Endpoint tests for /employee"""


def test_some_parameter(client, mocked_search):
    """
    GIVEN library.data.employee.search has a spy and a value for some parameter
    WHEN GET /employee is called with the some_parameter set to the some parameter value
    THEN library.data.employee.search is called with no parameters.
    """
    client.get('/employee?some_parameter=value 1')

    # Checking search call
    mocked_search.assert_called_once_with()


def test_join_date(client, mocked_search):
    """
    GIVEN library.data.employee.search has a spy and a date
    WHEN GET /employee is called with the join_date set to the date
    THEN library.data.employee.search is called with the join date.
    """
    client.get('/employee?join_date=2000-01-01')

    # Checking search call
    mocked_search.assert_called_once_with(join_date='2000-01-01')


def test_business_unit(client, mocked_search):
    """
    GIVEN library.data.employee.search has a spy and a business unit
    WHEN GET /employee is called with the business_unit set to the business unit
    THEN library.data.employee.search is called with the business unit.
    """
    client.get('/employee?business_unit=business unit 1')

    # Checking search call
    mocked_search.assert_called_once_with(business_unit='business unit 1')


def test_city(client, mocked_search):
    """
    GIVEN library.data.employee.search has a spy and a city
    WHEN GET /employee is called with the city set to the city
    THEN library.data.employee.search is called with the city.
    """
    client.get('/employee?city=city 1')

    # Checking search call
    mocked_search.assert_called_once_with(city='city 1')
