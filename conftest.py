"""
Pytest configuration file with shared fixtures for third_eye project
"""
import pytest
import os
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    """Setup test database configuration"""
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }


@pytest.fixture
def server_url():
    """Server URL for UI tests"""
    return os.getenv('SERVER_URL', 'http://127.0.0.1:8000')


@pytest.fixture
def test_user_credentials():
    """Test user credentials for authentication tests"""
    return {
        'username': 'testuser',
        'password': 'testpass123',
        'email': 'testuser@example.com'
    }


@pytest.fixture
def authenticated_client(client, django_user_model, test_user_credentials):
    """Django client with authenticated user"""
    user = django_user_model.objects.create_user(
        username=test_user_credentials['username'],
        password=test_user_credentials['password'],
        email=test_user_credentials['email']
    )
    client.force_login(user)
    return client
