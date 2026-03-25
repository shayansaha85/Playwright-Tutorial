from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage
from playwright.sync_api import Page, expect
import pytest

PHRASES = [
      'panda',
      'rainbow',
      'chocolate',
      'kolkata'
]

@pytest.mark.parametrize('phrase', PHRASES)
def test_basic_duckduckgo_searcg(phrase : str, page: Page, search_page : DuckDuckGoSearchPage, result_page : DuckDuckGoResultPage) -> None:

      search_page.load()
      search_page.search(phrase)

      expect(result_page.search_input).to_have_value(phrase)
      assert result_page.result_link_titles_contain_phrase(phrase)
      expect(page).to_have_title(f'{phrase} at DuckDuckGo')