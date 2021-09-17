from unittest.mock import Mock, patch
from services import get_todos

# 3
def test_request_response():
    # response = requests.get('http://jsonplaceholder.typicode.com/todos')
    response = get_todos()

    # Confirm that the request-response cycle completed successfully.
    assert response.ok, True

# 4
@patch('services.requests.get')
def test_getting_todos(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert response != None

# 5
def test_another_getting_todos():
    mock_get_patcher = patch('services.requests.get')

    # Start patching `requests.get`.
    mock_get = mock_get_patcher.start()
    mock_get.return_value.ok = True

    response = get_todos()

    mock_get_patcher.stop()

    assert response != None

# 7
@patch('services.requests.get')
def test_getting_todos_when_response_is_ok(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]

    # request.get() trả ra một đối tượng Response 
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = todos

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert response.json() == todos

@patch('services.requests.get')
def test_getting_todos_when_response_is_not_ok(mock_get):
    mock_get.return_value.ok = False
    response = get_todos()
    assert (response is None)