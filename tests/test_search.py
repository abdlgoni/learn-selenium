from ast import keyword
import pytest
from pages.home_pages import HomePage
from pages.search_page import SearchPage
from pages.search_result import SearchResult
from pages.article_page import ArticlePage
from utils.config import Config
import logging

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("driver")
class TestSearch:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.homepage = HomePage(self.driver)
        self.searchpage = SearchPage(self.driver)
        self.searchresult = SearchResult(self.driver)
        self.articlepage = ArticlePage(self.driver)
        logger.info("Setup complete")
        
        
    @pytest.mark.smoke
    def test_search_valid_keyword(self):
        """Test search dengan keyword valid"""
        logger.info("Starting: test_search_valid_keyword")
        
        # Open dan search
        self.homepage.open()
        keyword = "list programming languages"
        self.searchpage.search(keyword)
        logger.info(f"Searched: {keyword}")
        
        
        # Scenario: Langsung ke artikel
        
        if self.articlepage.is_article_loaded():
            article_title = self.articlepage.get_article_title()
            assert any("programming" in article_title.lower() and "language" in article_title.lower()), \
                f"Judul artikel '{article_title}' tidak mengandung kata kunci yang diharapkan."
            logger.info(f"✓ Direct to article: {article_title}")
        
        # Scenario: Ke search results
        else:
            # Verify results exist
            self.searchresult.wait_for_results()
            results_count = self.searchresult.get_results_count()
            
            assert results_count > 0, "No search results found"
            logger.info(f"✓ Found {results_count} results")
            
            result_titles = self.searchresult.get_result_title()
            assert "programming" in result_titles.lower() and "language" in result_titles.lower(), \
                "No result titles contain expected keywords"
            
            # Click first result
            self.searchresult.click_result(0)
            logger.info("✓ Clicked first result")
            
            # Verify article loaded
            assert self.articlepage.is_article_loaded(), \
                "Article failed to load"
            
            article_title = self.articlepage.get_article_title()
            logger.info(f"✓ Article opened: {article_title}")
        
        logger.info("Test PASSED ✓")
            
    
    @pytest.mark.parametrize("search_input_data",[
        "adsjasdjfha",
        "!!!!!!!!!!",
        "seleniumverylongkeyword"
    ])
    def test_search_invalid_keyword(self, search_input_data):
        """
        TC-007: Search dengan keyword yang tidak ditemukan
        
        Steps:
            1. Buka homepage
            2. Search [search_input_data]
            3. Verify no results message
            4. Verify page title
            5. Check suggestion (optional)
        
        Expected:
            - "No results" message ditampilkan
            - Judul halaman != keyword
            - Halaman search results (bukan article)
        """
        # Step 1: Open homepage
        self.homepage.open()
        
        # Perform search
        keyword = search_input_data
        self.searchpage.search(keyword)
        
        # Verify no results message
        is_no_results = self.searchresult.is_no_results_displayed()
        assert is_no_results, \
            "Expected 'no results' message untuk keyword invalid, tapi tidak muncul"
        
        # Verify page title (tidak sama dengan keyword)
        page_title = self.searchresult.get_title()
        assert page_title != keyword, \
            f"Page title seharusnya BUKAN '{keyword}', tapi dapat: '{page_title}'"
        
        #  Verify URL
        current_url = self.searchresult.get_current_url()
        assert "search=" in current_url.lower() or "special:search" in current_url.lower(), \
            f"Expected URL search results, tapi dapat: {current_url}"
        
        # Step 6: Additional check - verify results count = 0
        results_count = self.searchresult.get_results_count()
        assert results_count == 0, \
            f"Expected 0 results, tapi dapat: {results_count}"
        
        # Step 7: Check suggestion (optional, untuk logging)
        suggestion = self.searchresult.get_did_you_mean_suggestion()
        if suggestion:
            print(f"ℹ️  Wikipedia suggests: '{suggestion}'")
        else:
            print("ℹ️  No suggestion provided by Wikipedia")

    
    @pytest.mark.regression
    def test_search_and_verify_article_content(self):
        """ Search dan verifikasi konten artikel"""

        self.homepage.open()

        keyword = "Python (programming language)"
        self.searchpage.search(keyword)

        # Verify article loaded
        assert self.articlepage.is_article_loaded(), "Article page not loaded"

        # Verify title exact match
        article_title = self.articlepage.get_article_title()
        assert article_title == keyword, \
            f"Expected title '{keyword}', but got '{article_title}'"

        # Verify TOC
        assert self.articlepage.is_toc_displayed(), \
            "Table of Contents not displayed"

        # Verify content
        first_paragraph = self.articlepage.get_first_paragraph()
        assert first_paragraph, "First paragraph is empty"

        words_to_check = ["python", "programming", "language"]
        assert all(word in first_paragraph.lower() for word in words_to_check), \
            f"Expected words {words_to_check} not found in first paragraph"

        
    
       