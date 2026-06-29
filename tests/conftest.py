from copy import deepcopy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def reset_activities():
    """Save and restore the module-level `activities` dict around each test."""
    original = deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)
