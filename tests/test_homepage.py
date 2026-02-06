"""
Test cases untuk Wikipedia Homepage
TC-001, TC-002, TC-003
"""

import pytest
from pages.home_pages import HomePage
from utils.config import Config
import logging


logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("driver")
class TestHomePage:
    """Test class untuk Wikipedia Homepage"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """
        Setup untuk setiap test
        
        Args:
            driver: WebDriver instance dari conftest
        """
        self.driver = driver
        self.home_page = HomePage(driver)
        logger.info("=" * 80)
        logger.info("Setup completed for HomePage test")
    
    @pytest.mark.smoke
    def test_TC001_verify_homepage_opens(self):
        """
        TC-001: Verifikasi halaman utama Wikipedia terbuka
        
        Steps:
            1. Buka https://www.wikipedia.org
            2. Verifikasi page title
            3. Verifikasi logo ditampilkan
        
        Expected:
            - Title mengandung "Wikipedia"
            - Logo Wikipedia tampil
        """
        logger.info("Starting TC-001: Verify homepage opens")
        
        # Step 1: Buka homepage
        self.home_page.open()
        
        # Step 2: Verifikasi title
        title = self.home_page.get_page_title()
        assert "Wikipedia" in title, f"Expected 'Wikipedia' in title, but got: {title}"
        logger.info(f"✓ Page title verified: {title}")
        
        # Step 3: Verifikasi logo
        assert self.home_page.is_logo_displayed(), "Wikipedia logo tidak ditampilkan"
        logger.info("✓ Wikipedia logo is displayed")
        
        logger.info("TC-001 PASSED ✓")
    
    @pytest.mark.smoke
    def test_TC002_verify_available_languages(self):
        """
        TC-002: Verifikasi bahasa yang tersedia di homepage
        
        Steps:
            1. Buka homepage
            2. Hitung jumlah bahasa yang tersedia
            3. Verifikasi bahasa populer tersedia
        
        Expected:
            - Ada minimal 10 bahasa populer tersedia
            - Bahasa seperti English, Español, Deutsch, dll tersedia
        """
        logger.info("Starting TC-002: Verify available languages")
        
        # Step 1: Buka homepage
        self.home_page.open()
        
        # Step 2: Hitung bahasa
        language_count = self.home_page.get_language_count()
        assert language_count >= 10, f"Expected at least 10 languages, but found: {language_count}"
        logger.info(f"✓ Found {language_count} languages")
        
        # Step 3: Verifikasi bahasa populer
        popular_languages = ['en', 'es', 'de', 'fr', 'ja', 'ru', 'it', 'zh', 'pt']
        
        for lang in popular_languages:
            assert self.home_page.is_language_available(lang), f"Language {lang} tidak tersedia"
            logger.info(f"✓ Language '{lang}' is available")
        
        logger.info(f"TC-002 PASSED ✓ - Total {language_count} languages verified")
    
    @pytest.mark.smoke
    def test_TC003_access_english_wikipedia(self):
        """
        TC-003: Akses Wikipedia versi English
        
        Steps:
            1. Buka homepage
            2. Click English language link
            3. Verifikasi redirect ke en.wikipedia.org
        
        Expected:
            - Redirect ke https://en.wikipedia.org
            - URL contains "en.wikipedia.org"
        """
        logger.info("Starting TC-003: Access English Wikipedia")
        
        # Step 1: Buka homepage
        self.home_page.open()
        
        # Step 2: Click English link
        self.home_page.click_english_link()
        
        # Step 3: Verifikasi URL
        current_url = self.home_page.get_current_url()
        assert "en.wikipedia.org" in current_url, f"Expected 'en.wikipedia.org' in URL, but got: {current_url}"
        logger.info(f"✓ Successfully redirected to: {current_url}")
        
        # Additional verification - page title
        page_title = self.home_page.get_page_title()
        assert "Wikipedia" in page_title, f"Expected 'Wikipedia' in title, but got: {page_title}"
        logger.info(f"✓ English Wikipedia page title: {page_title}")
        
        logger.info("TC-003 PASSED ✓")
    
    @pytest.mark.regression
    def test_homepage_subtitle_verification(self):
        """
        Additional Test: Verifikasi subtitle "The Free Encyclopedia"
        
        Steps:
            1. Buka homepage
            2. Get subtitle text
            3. Verifikasi text
        
        Expected:
            - Subtitle contains "The Free Encyclopedia"
        """
        logger.info("Starting Test: Homepage subtitle verification")
        
        # Step 1: Buka homepage
        self.home_page.open()
        
        # Step 2 & 3: Verifikasi subtitle
        subtitle = self.home_page.get_subtitle_text()
        assert "The Free Encyclopedia" in subtitle, f"Expected 'The Free Encyclopedia', but got: {subtitle}"
        logger.info(f"✓ Subtitle verified: {subtitle}")
        
        logger.info("Subtitle verification PASSED ✓")
    
    @pytest.mark.regression
    def test_search_input_available(self):
        """
        Additional Test: Verifikasi search input tersedia
        
        Steps:
            1. Buka homepage
            2. Verifikasi search input ditampilkan
        
        Expected:
            - Search input visible dan clickable
        """
        logger.info("Starting Test: Search input availability")
        
        # Step 1: Buka homepage
        self.home_page.open()
        
        # Step 2: Verifikasi search input
        assert self.home_page.is_search_input_displayed(), "Search input tidak ditampilkan"
        logger.info("✓ Search input is displayed")
        
        logger.info("Search input availability PASSED ✓")
    
    @pytest.mark.regression
    def test_multiple_language_links(self):
        """
        Additional Test: Verifikasi multiple language dapat diakses
        
        Steps:
            1. Buka homepage
            2. Verifikasi beberapa language link
        
        Expected:
            - Semua popular language links dapat diakses
        """
        logger.info("Starting Test: Multiple language links")
        
        # Step 1: Buka homepage
        self.home_page.open()
        
        # Step 2: Verifikasi multiple languages
        test_languages = {
            'en': 'English',
            'es': 'Español',
            'de': 'Deutsch',
            'fr': 'Français',
            'ja': '日本語'
        }
        
        for lang_code, lang_name in test_languages.items():
            assert self.home_page.is_language_available(lang_code), f"Language {lang_name} tidak tersedia"
            logger.info(f"✓ {lang_name} ({lang_code}) is available")
        
        logger.info("Multiple language links PASSED ✓")
    
    @pytest.mark.smoke
    def test_homepage_complete_verification(self):
        """
        Additional Test: Complete homepage verification
        
        Steps:
            1. Buka homepage
            2. Verifikasi semua elemen penting
        
        Expected:
            - Semua elemen homepage loaded dengan baik
        """
        logger.info("Starting Test: Complete homepage verification")
        
        # Step 1: Buka homepage
        self.home_page.open()
        
        # Step 2: Comprehensive verification
        assert self.home_page.verify_homepage_loaded(), "Homepage verification failed"
        logger.info("✓ All homepage elements verified successfully")
        
        logger.info("Complete homepage verification PASSED ✓")
    
    @pytest.mark.parametrize("lang_code,expected_url_part", [
        ("en", "en.wikipedia.org"),
        ("es", "es.wikipedia.org"),
        ("de", "de.wikipedia.org"),
        ("fr", "fr.wikipedia.org"),
    ])
    def test_language_navigation(self, lang_code, expected_url_part):
        """
        Parametrized Test: Test navigasi ke berbagai bahasa
        
        Args:
            lang_code (str): Language code
            expected_url_part (str): Expected URL fragment
        """
        logger.info(f"Starting parametrized test for language: {lang_code}")
        
        # Buka homepage
        self.home_page.open()
        
        # Click language link
        self.home_page.click_language_by_code(lang_code)
        
        # Verifikasi URL
        current_url = self.home_page.get_current_url()
        assert expected_url_part in current_url, f"Expected {expected_url_part} in URL, but got: {current_url}"
        logger.info(f"✓ Successfully navigated to {lang_code}: {current_url}")