from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

class SearchResult(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)
        
    RESULT_CONTAINER = (By.CSS_SELECTOR, ".searchresults")
    RESULT_ITEM = (By.CSS_SELECTOR, ".mw-search-result")
    RESULT_TITLES = (By.CSS_SELECTOR, ".mw-search-result-heading a")
    RESULT_SNIPPETS = (By.CSS_SELECTOR, ".searchresult")
    
    NO_RESULT_MESSAGE = (By.CSS_SELECTOR, ".mw-search-nonefound")
    
    DID_YOU_MEAN_LINK = (By.CSS_SELECTOR, ".searchdidyoumean")
    
    NEXT_PAGE_LINK = (By.CSS_SELECTOR, "a[rel='next']")
    PREV_PAGE_LINK = (By.CSS_SELECTOR, "a[rel='prev']")
    
    def get_results_count(self):
        results = self.find_elements(self.RESULT_ITEM)
        count = len(results)
        self.logger.info(f"Search results count: {count}")
        return count
    
    def get_result_title(self):
        titles = self.find_elements(self.RESULT_TITLES)
        title_texts = [t.text for t in titles]
        self.logger.info(f"Result titles: {title_texts}")
        return title_texts
    
    def click_result(self, index=0):
        """Click hasil search berdasarkan index"""
        titles = self.find_elements(self.RESULT_TITLES)
        if index < len(titles):
            titles[index].click()
            self.logger.info(f"Clicked result at index {index}")
        else:
            raise IndexError(f"Result index {index} out of range")
        
    def wait_for_results(self):
        self.is_element_visible(self.RESULT_CONTAINER, timeout=10)

    
    def is_no_results_displayed(self):
        return self.is_element_visible(self.NO_RESULT_MESSAGE, timeout=3)
    
    def get_did_you_mean_suggestion(self):
        if self.is_element_visible(self.DID_YOU_MEAN_LINK, timeout=3):
            return self.get_text(self.DID_YOU_MEAN_LINK)
        return None
    
    