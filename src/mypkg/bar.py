from typing import List
from mypkg.dummy_class import dummy_class
from mypkg.foo import foo

def bar(my_list_of_lists: List[List[dummy_class]]) -> None:
    for my_list in my_list_of_lists:
        foo(my_list)