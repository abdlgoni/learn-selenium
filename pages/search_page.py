from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.config import Config
import logging

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL
        self.logger = logging.getLogger(__name__)
        
    
    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SEARCH_SUGESTION = (By.ID, "typeahead-suggestions")
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, ".suggestions-dropdown")
    
    SUGESTION_ITEM = (By.CSS_SELECTOR, ".suggestion-link")
    SUGESTION_TITLE = (By.CSS_SELECTOR, ".suggestion-title")
    SUGESTION_DESCRIPTION = (By.CSS_SELECTOR, ".suggestion-description")
    
    def enter_search_text(self, text):
        self.input_text(self.SEARCH_INPUT, text)
        self.logger.info(f"entered search text: {text}")
        
    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)
        self.logger.info(f"clicked search button")
        
    def search(self, text):
        self.enter_search_text(text)
        self.click_search_button()
        self.logger.info(f"performed search: {text}")
        
    def search_and_enter(self, text):
        search_input = self.find_elements(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(text)
        search_input.send_keys(Keys.RETURN)
        self.logger.info(f"searched with enter key: {text}")
        
    def is_suggestion_displayed(self):
        return self.is_element_visible(self.SEARCH_DROPDOWN, timeout=3)
    
    def click_suggestion(self, index=0):
        sugestions = self.find_elements(self.SUGESTION_ITEM)
        if index < len(sugestions):
            sugestions[index].click()
            self.logger.info(f"clicked sugestion at index {index}")
        else:
            raise IndexError(f"sugestion index {index} out of range")
        
    def click_suggestion_by_text(self, text):
        suggestions = self.find_elements(self.SUGESTION_ITEM)
        for suggestion in suggestions:
            if text.lower() in suggestion.text.lower():
                suggestion.click()
            return
        raise ValueError(f"suggetions {text} not found")
    
    def is_search_input_displayed(self):
        return self.is_element_visible(self.SEARCH_INPUT)
    
    def get_search_placeholder(self):
        return self.get_attribute(self.SEARCH_INPUT, "Placeholder")
    
    def clear_search_input(self):
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.clear()
        self.logger.info(f"cleared search input")
     
        
    