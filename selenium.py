import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

create_name = 'Moderator'
create_roomName = 'Scrum'
create_deck = 'Starter Deck'

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True


@pytest.fixture
@pytest.mark.nondestructive
def firefox_options(firefox_options):
    firefox_options.binary = '/usr/bin/firefox'
    firefox_options.add_argument('--headless')
    return firefox_options


# check the site opens
@pytest.mark.nondestructive
def test_page_title(selenium, base_url):
    selenium.get(base_url + ':80')
    assert 'ScrumMaster' in selenium.title


# function to check the poker site
@pytest.mark.nondestructive
def test_poker_site(selenium, base_url):
    selenium.get(base_url)
    selenium.find_element_by_link_text("Poker").click()

    time.sleep(10)

    assert base_url + '/#/poker' in selenium.current_url

    return selenium.current_url


# function to create and join a new room as moderator
@pytest.mark.nondestructive
def test_scenario_create_room(selenium, base_url):
    # opens the site and fill in the name
    selenium.get(test_poker_site(selenium, base_url))
    time.sleep(3)
    name = selenium.find_element_by_xpath('//input[@formcontrolname="nickName"]')
    name.clear()
    name.send_keys(create_name)

    # fill in the room_name
    room_name = selenium.find_element_by_xpath('//input[@formcontrolname="roomName"]')
    room_name.clear()
    room_name.send_keys(create_roomName)

    # choose the deck
    deck = Select(selenium.find_element_by_xpath('//select[@formcontrolname="prop"]'))
    deck.select_by_visible_text(create_deck)

    # press the create button and check if the site is changing
    selenium.find_element_by_xpath('//button[@class="btn btn-block btn-primary"]').click()
    time.sleep(3)
    assert base_url + '/#/poker/game/' in selenium.current_url

    # check whether the entries are transferred correctly
    proof_room_name = selenium.find_element_by_tag_name('h1')
    assert proof_room_name.text == create_roomName

    proof_name = selenium.find_element_by_xpath('//div[@class="col-7 name my-auto pl-2"]')
    assert proof_name.text == create_name + ' Moderator'

    proof_deck = selenium.find_element_by_tag_name('p')
    assert proof_deck.text == 'Deck: ' + create_deck
