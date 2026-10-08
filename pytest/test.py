"""Tests unitaires selenium du front (lancer `npm run dev` avant, puis `pytest` dans ce dossier)"""
import pytest

from global_variable import (
    HOME_BUTTONS,
    HOME_TITLE,
    LIST_OF_PAGE_BUTTON_ID,
)
from scrapper import Scrapper


@pytest.fixture(scope="session")
def browser():
    """Un seul navigateur pour toute la session de tests"""
    scrapper = Scrapper(headless=True)
    yield scrapper
    scrapper.quit()


@pytest.fixture
def scrapper(browser):
    """Chaque test repart de la page d'accueil"""
    browser.open_home_page()
    return browser


def test_home_page_title(scrapper):
    """A function that check the title of the home page"""
    assert scrapper.get_title() == HOME_TITLE


def test_home_page_has_h1(scrapper):
    """A function that check the home page has its (hidden) main title"""
    scrapper.get_element("WorldMapPageButton")
    assert scrapper.count_elements("h1") == 1


def test_home_page_has_all_buttons(scrapper):
    """A function that check that the home page has exactly one button per page"""
    for page_id in LIST_OF_PAGE_BUTTON_ID:
        scrapper.get_element(page_id)
    assert scrapper.count_elements("nav[aria-label='Pages du site'] a") == len(LIST_OF_PAGE_BUTTON_ID)


@pytest.mark.parametrize("page_id,label,path", HOME_BUTTONS)
def test_check_page_button_label(scrapper, page_id, label, path):
    """A function that check the label of each home page button"""
    assert scrapper.get_id_of_an_element(page_id) == label


@pytest.mark.parametrize("page_id,label,path", HOME_BUTTONS)
def test_button_link_target(scrapper, page_id, label, path):
    """A function that check the href of each home page button"""
    href = scrapper.get_element(page_id).get_attribute("href")
    assert href.endswith(path)


@pytest.mark.parametrize("page_id,label,path", HOME_BUTTONS)
def test_click_on_button_change_page(scrapper, page_id, label, path):
    """A function that check that clicking on a button go to the right page"""
    scrapper.click_on_element(page_id)
    assert scrapper.wait_for_path(path)


def test_go_back_home(scrapper):
    """A function that check that the browser back button return to the home page"""
    scrapper.click_on_element("AboutPageButton")
    scrapper.wait_for_path("/About")
    scrapper.go_back()
    assert scrapper.get_id_of_an_element("AboutPageButton") == "À propos"


def test_unknown_route_show_home_page(scrapper):
    """A function that check that an unknown url fall back on the home page"""
    scrapper.driver.get(scrapper.driver.current_url + "page-qui-n-existe-pas")
    assert scrapper.get_id_of_an_element("WorldMapPageButton") == "Explorer la Map"
