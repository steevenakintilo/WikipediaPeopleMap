
from global_variable import *
from scrapper import *

import pytest

scrapper = Scrapper(True)
scrapper.open_home_page()

@pytest.mark.parametrize("page_id")
def test_check_page_id(page_id):
    """A function that check if all page id of the home page are correct"""

    assert scrapper.get_id_of_an_element(page_id) in LIST_OF_PAGE_BUTTON_NAME

def test_go_back_home_button(page_id):
    """A function that check if the go back home button work fine"""

    assert scrapper.get_id_of_an_element(page_id) in LIST_OF_PAGE_BUTTON_NAME
