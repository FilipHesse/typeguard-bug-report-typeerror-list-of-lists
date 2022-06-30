"""Tests for UpliftVisualization."""
import pytest
from src.mypkg.dummy_class import dummy_class
from src.mypkg.foo import foo
from src.mypkg.bar import bar

def test_bar(
    example_dummy: dummy_class,
) -> None:
    '''Test bar'''
    bar([[example_dummy],[example_dummy]])

def test_foo(
    example_dummy: dummy_class,
) -> None:
    '''Test foo'''
    foo([example_dummy])
