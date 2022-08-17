import pytest

from kiwi.app import create_app


@pytest.fixture(scope='session')
def app():
	"""
	Setup Flask test app. Only executed once.

	:return: Flask app
	"""
	params = {
		'DEBUG': False,
		'TESTING': True,
	}

	_app = create_app(settings_override=params)

	# Establish app context before running tests
	ctx = _app.app_context()
	ctx.push()

	yield _app

	ctx.pop()


@pytest.fixture(scope='function')
def client(app):
	"""
	Setup client. Executed for each test function.

	:param app: Pytest fixture
	:return: Flask app client
	"""
	yield app.test_client()
