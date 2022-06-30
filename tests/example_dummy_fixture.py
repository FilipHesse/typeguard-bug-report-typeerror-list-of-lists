import pytest

from src.mypkg.dummy_class import dummy_class

@pytest.fixture
def example_dummy() -> dummy_class:
    return dummy_class(1)
