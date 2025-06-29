from selenium import webdriver
from parsers.quote_selection_selenium.config import Config
from parsers.quote_selection_selenium.services.user_interaction_service import UserInteractionService



def run():
    config = Config()
    
    chrome = webdriver.Chrome()
    chrome.get(config.url)
    
    UserInteractionService(browser_object = chrome).prompt_for_search()


if __name__ == '__main__':
    run()
