from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

class ArticlePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)
        
    ARTICLE_TITLE = (By.ID, "firstHeading")
    ARTICLE_SUBTITLE = (By.CSS_SELECTOR, ".mw-page-title-main")
    
    # TOC_BUTTON = (By.ID, "vector-page-titlebar-toc-label")
    TOC_CONTAINER = (By.ID, "vector-toc")
    TOC_TITLE = (By.CSS_SELECTOR, ".vector-pinnable-header-label > h2")
    # TOC_LIST = (By.CSS_SELECTOR, ".vector-toc-contents")
    TOC_LINKS = (By.CSS_SELECTOR, "a.vector-toc-link")
    
    ARTICLE_CONTENT = (By.CSS_SELECTOR, ".mw-parser-output")
    ARTICLE_PARAGRAPHS = (By.CSS_SELECTOR, ".mw-parser-output > p")
    
    def get_article_title(self):
        title = self.get_text(self.ARTICLE_TITLE)
        self.logger.info(f"article title {title}")
        return title
    
    def is_article_loaded(self):
        is_loaded = self.is_element_visible(self.ARTICLE_SUBTITLE)
        self.logger.debug(f"article loaded {is_loaded}")
        return is_loaded
    
    def get_first_paragraph(self):
        """
        Get first non-empty paragraph text
        """
        paragraphs = self.find_elements(self.ARTICLE_PARAGRAPHS)

        for p in paragraphs:
            text = p.text.strip()
            if text:
                self.logger.info(f"First paragraph: {text[:80]}...")
                return text

        self.logger.warning("No non-empty paragraph found")
        return ""

    
    def is_content_available(self):
        """Check apakah artikel punya content"""
        return self.is_element_visible(self.ARTICLE_CONTENT)
    
    def is_toc_displayed(self):
        return self.is_element_visible(self.TOC_CONTAINER)
    
    def get_toc_title(self):
        title = self.get_text(self.TOC_TITLE)
        self.logger.info(f"table of contents title {title}")
        return title
    
    def get_toc_items(self):
        links = self.find_elements(self.TOC_LINKS)
        toc_items = [link.text for link in links]
        self.logger.info(f"table of contents items: {toc_items}")
        return toc_items
    
    def click_toc_item(self, item_text):
        links = self.find_elements(self.TOC_LINKS)
        for link in links:
            if link.text.strip().lower() == item_text.strip().lower():
                link.click()
                self.logger.info(f"clicked TOC item: {item_text}")
                return
        raise ValueError(f"TOC item '{item_text}' not found")
    
    
        
    