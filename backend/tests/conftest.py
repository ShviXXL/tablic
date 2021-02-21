"""Pytest fixtures."""

# pylint: disable=redefined-outer-name

import pytest
from bson.objectid import ObjectId


@pytest.fixture
def secret(faker):
    """Random secret key."""
    return faker.password(32)


@pytest.fixture
def password(faker):
    """Random password."""
    return faker.password(16)


@pytest.fixture
def time_delta(faker):
    """Time delta."""
    return faker.time_delta(1)


@pytest.fixture
def object_id():
    """Random uuid."""
    return ObjectId()