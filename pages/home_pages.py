"""
Page Object Model untuk Wikipedia Homepage (wikipedia.org)
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config
import logging


class HomePage(BasePage):
    """Page Object untuk Wikipedia Homepage"""
    
    def __init__(self, driver):
        """
        Initialize HomePage
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
        self.url = Config.BASE_URL
        self.logger = logging.getLogger(__name__)
    
    # ========== Locators ==========
    
    # Logo & Branding
    WIKIPEDIA_LOGO = (By.CSS_SELECTOR, ".central-textlogo")
    WIKIPEDIA_WORDMARK = (By.CSS_SELECTOR, ".central-textlogo__image")
    SITE_SUBTITLE = (By.CSS_SELECTOR, ".central-textlogo-wrapper strong")
    
    # Search
    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    # Language Links
    LANGUAGE_LINKS = (By.CSS_SELECTOR, ".central-featured-lang")
    ENGLISH_LINK = (By.XPATH, "//a[@id='js-link-box-en']")
    SPANISH_LINK = (By.XPATH, "//a[@id='js-link-box-es']")
    GERMAN_LINK = (By.XPATH, "//a[@id='js-link-box-de']")
    FRENCH_LINK = (By.XPATH, "//a[@id='js-link-box-fr']")
    JAPANESE_LINK = (By.XPATH, "//a[@id='js-link-box-ja']")
    RUSSIAN_LINK = (By.XPATH, "//a[@id='js-link-box-ru']")
    ITALIAN_LINK = (By.XPATH, "//a[@id='js-link-box-it']")
    CHINESE_LINK = (By.XPATH, "//a[@id='js-link-box-zh']")
    PORTUGUESE_LINK = (By.XPATH, "//a[@id='js-link-box-pt']")
    ARABIC_LINK = (By.XPATH, "//a[@id='js-link-box-ar']")
    
    # Language selector
    LANGUAGE_SEARCH_INPUT = (By.ID, "searchLanguage")
    
    # Footer
    READ_WIKIPEDIA_LINK = (By.LINK_TEXT, "Read Wikipedia in your language")
    
    # Other languages section
    OTHER_LANGUAGES_SECTION = (By.CSS_SELECTOR, ".other-projects")
    
    # ========== Page Actions ==========
    
    def open(self):
        """
        Open Wikipedia homepage
        """
        self.open_url(self.url)
        self.wait_for_page_load()
        self.logger.info(f"Opened Wikipedia homepage: {self.url}")
    
    def get_page_title(self):
        """
        Get page title
        
        Returns:
            str: Page title
        """
        title = self.get_title()
        self.logger.debug(f"Page title: {title}")
        return title
    
    def is_logo_displayed(self):
        """
        Check apakah Wikipedia logo ditampilkan
        
        Returns:
            bool: True jika logo visible
        """
        is_displayed = self.is_element_visible(self.WIKIPEDIA_LOGO)
        self.logger.debug(f"Logo displayed: {is_displayed}")
        return is_displayed
    
    def get_subtitle_text(self):
        """
        Get subtitle text (The Free Encyclopedia)
        
        Returns:
            str: Subtitle text
        """
        subtitle = self.get_text(self.SITE_SUBTITLE)
        self.logger.debug(f"Subtitle: {subtitle}")
        return subtitle
    
    # ========== Search Methods ==========
    
    def enter_search_text(self, search_text):
        """
        Enter text ke search input
        
        Args:
            search_text (str): Text untuk search
        """
        self.input_text(self.SEARCH_INPUT, search_text)
        self.logger.info(f"Entered search text: {search_text}")
    
    def click_search_button(self):
        """
        Click search button
        """
        self.click(self.SEARCH_BUTTON)
        self.logger.info("Clicked search button")
    
    def search(self, search_text):
        """
        Perform search (enter text + click button)
        
        Args:
            search_text (str): Text untuk search
        """
        self.enter_search_text(search_text)
        self.click_search_button()
        self.logger.info(f"Performed search: {search_text}")
    
    def is_search_input_displayed(self):
        """
        Check apakah search input ditampilkan
        
        Returns:
            bool: True jika search input visible
        """
        return self.is_element_visible(self.SEARCH_INPUT)
    
    # ========== Language Methods ==========
    
    def get_all_language_links(self):
        """
        Get semua language links yang ditampilkan
        
        Returns:
            list: List of WebElements untuk language links
        """
        links = self.find_elements(self.LANGUAGE_LINKS)
        self.logger.debug(f"Found {len(links)} language links")
        return links
    
    def get_language_count(self):
        """
        Get jumlah bahasa yang tersedia di homepage
        
        Returns:
            int: Jumlah bahasa
        """
        count = len(self.get_all_language_links())
        self.logger.debug(f"Language count: {count}")
        return count
    
    def click_english_link(self):
        """
        Click English language link
        """
        self.click(self.ENGLISH_LINK)
        self.logger.info("Clicked English language link")
    
    def click_spanish_link(self):
        """
        Click Spanish language link
        """
        self.click(self.SPANISH_LINK)
        self.logger.info("Clicked Spanish language link")
    
    def click_german_link(self):
        """
        Click German language link
        """
        self.click(self.GERMAN_LINK)
        self.logger.info("Clicked German language link")
    
    def click_language_by_code(self, lang_code):
        """
        Click language link berdasarkan language code
        
        Args:
            lang_code (str): Language code (en, es, de, fr, etc.)
        """
        locator = (By.XPATH, f"//a[@id='js-link-box-{lang_code}']")
        self.click(locator)
        self.logger.info(f"Clicked language link: {lang_code}")
    
    def is_language_available(self, lang_code):
        """
        Check apakah bahasa tersedia
        
        Args:
            lang_code (str): Language code (en, es, de, etc.)
            
        Returns:
            bool: True jika bahasa tersedia
        """
        locator = (By.XPATH, f"//a[@id='js-link-box-{lang_code}']")
        is_available = self.is_element_present(locator)
        self.logger.debug(f"Language {lang_code} available: {is_available}")
        return is_available
    
    def get_language_link_text(self, lang_code):
        """
        Get text dari language link
        
        Args:
            lang_code (str): Language code
            
        Returns:
            str: Text dari language link
        """
        locator = (By.XPATH, f"//a[@id='js-link-box-{lang_code}']")
        text = self.get_text(locator)
        self.logger.debug(f"Language {lang_code} text: {text}")
        return text
    
    # ========== Verification Methods ==========
    
    def verify_homepage_loaded(self):
        """
        Verify bahwa homepage sudah loaded dengan baik
        
        Returns:
            bool: True jika homepage loaded successfully
        """
        try:
            # Check multiple elements untuk memastikan page loaded
            checks = [
                self.is_logo_displayed(),
                self.is_search_input_displayed(),
                self.get_language_count() > 0
            ]
            
            result = all(checks)
            self.logger.info(f"Homepage verification: {result}")
            return result
        except Exception as e:
            self.logger.error(f"Homepage verification failed: {str(e)}")
            return False
    
    def get_popular_languages(self):
        """
        Get list of popular language codes yang tersedia
        
        Returns:
            list: List of language codes
        """
        popular_langs = ['en', 'es', 'de', 'fr', 'ja', 'ru', 'it', 'zh', 'pt', 'ar']
        available_langs = [lang for lang in popular_langs if self.is_language_available(lang)]
        self.logger.debug(f"Available popular languages: {available_langs}")
        return available_langs