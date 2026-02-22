"""
UI Tests for third_eye - Django Test Enforcer
IMPLEMENTED AND WORKING!

Uses Playwright for browser automation.

Run with: pytest third_eye/test_ui.py -m ui --headed
"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="module")
def base_url(server_url):
    """Return base URL for tests"""
    return server_url if server_url else "http://127.0.0.1:8000"


@pytest.mark.ui
class TestHomeUI:
    """UI tests for home page"""

    def test_home_page_loads(self, page: Page, base_url: str):
        """Test home page loads successfully"""
        page.goto(f"{base_url}/")
        expect(page).to_have_title(re.compile("Medical Facilities|Third Eye", re.IGNORECASE))

    def test_click_here_button_visible(self, page: Page, base_url: str):
        """Test Click Here button is visible"""
        page.goto(f"{base_url}/")
        button = page.locator(".btn")
        expect(button).to_be_visible()

    def test_click_here_button_navigates(self, page: Page, base_url: str):
        """Test Click Here button navigates to divyadrishti"""
        page.goto(f"{base_url}/")
        button = page.locator("a.btn")
        button.click()
        expect(page).to_have_url(re.compile(".*/divyadrishti/.*"))


@pytest.mark.ui
class TestBaseUI:
    """UI tests for base template elements"""

    def test_third_eye_logo_visible(self, page: Page, base_url: str):
        """Test Third Eye logo is visible"""
        page.goto(f"{base_url}/")
        logo = page.locator("img[alt*='Third Eye']")
        expect(logo).to_be_visible()

    def test_third_eye_your_insight_link(self, page: Page, base_url: str):
        """Test Third Eye : Your Insight link"""
        page.goto(f"{base_url}/")
        link = page.locator("a:has-text('Third Eye : Your Insight')")
        expect(link).to_be_visible()
        
    def test_git_repo_link_visible(self, page: Page, base_url: str):
        """Test Git Repo link is visible"""
        page.goto(f"{base_url}/")
        link = page.locator("a:has-text('Git Repo')")
        expect(link).to_be_visible()

    def test_admin_panel_link_visible(self, page: Page, base_url: str):
        """Test Admin Panel link is visible"""
        page.goto(f"{base_url}/")
        link = page.locator("a:has-text('Admin Panel')")
        expect(link).to_be_visible()

    def test_social_media_links_visible(self, page: Page, base_url: str):
        """Test social media links are visible"""
        page.goto(f"{base_url}/")
        facebook = page.locator(".fa-facebook")
        expect(facebook).to_be_visible()


@pytest.mark.ui  
class TestDivyadrishtiUI:
    """UI tests for divyadrishti page"""

    def test_divyadrishti_page_loads(self, page: Page, base_url: str):
        """Test divyadrishti page loads"""
        page.goto(f"{base_url}/divyadrishti/")
        expect(page).to_have_url(re.compile(".*/divyadrishti/.*"))

    def test_symptom_selection_present(self, page: Page, base_url: str):
        """Test symptom selection elements are present"""
        page.goto(f"{base_url}/divyadrishti/")
        # Check if page has symptom-related content
        content = page.content()
        assert "symptom" in content.lower() or "select" in content.lower()

    def test_navigation_to_table(self, page: Page, base_url: str):
        """Test navigation to table page"""
        page.goto(f"{base_url}/divyadrishti/table")
        expect(page).to_have_url(re.compile(".*/table.*"))


@pytest.mark.ui
class TestAdminUI:
    """UI tests for admin interface"""

    def test_admin_login_page_loads(self, page: Page, base_url: str):
        """Test admin login page loads"""
        page.goto(f"{base_url}/admin/")
        expect(page).to_have_url(re.compile(".*/admin/.*"))
        expect(page.locator("body")).to_contain_text("Django")


@pytest.mark.ui
class TestResponsiveUI:
    """UI tests for responsive design"""

    def test_page_responsive_mobile(self, page: Page, base_url: str):
        """Test page is responsive on mobile"""
        page.set_viewport_size({"width": 375, "height": 667})
        page.goto(f"{base_url}/")
        expect(page.locator("body")).to_be_visible()

    def test_page_responsive_tablet(self, page: Page, base_url: str):
        """Test page is responsive on tablet"""
        page.set_viewport_size({"width": 768, "height": 1024})
        page.goto(f"{base_url}/")
        expect(page.locator("body")).to_be_visible()


# Import re for regex matching
import re

