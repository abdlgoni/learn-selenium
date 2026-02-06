from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

class ArticlePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)
        
    ARTICLE_TITLE = (By.ID, "firstHeading")
    ARTICLE_SUBTITLE = (By.CSS_SELECTOR, ".mw-page-title-main")
    
    ARTICLE_CONTENT = (By.CSS_SELECTOR, ".mw-parser-output")
    ARTICLE_PARAGRAPHS = (By.CSS_SELECTOR, "mw-parser-output > p")
    
    def get_article_title(self):
        title = self.get_text(self.ARTICLE_TITLE)
        self.logger.info(f"article title {title}")
        return title
    
    def is_article_loaded(self):
        is_loaded = self.is_element_visible(self.ARTICLE_TITLE)
        self.logger.debug(f"article loaded {is_loaded}")
        return is_loaded
    
    
        
    