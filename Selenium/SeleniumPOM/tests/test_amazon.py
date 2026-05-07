import time

import pytest

from pages.home_page import HomePage
from pages.product_listing_page import ProductListPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    print("\nOpened Amazon Homepage. Title & URL verified.")



@pytest.mark.parametrize("searchproduct", [
    ("wireless mouse"), ("shoes")
])
def test_search_product(driver, searchproduct):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Search Product - {searchproduct}")
    homepage.click_search_button()
    print()

    assert homepage.is_amazon_page_loaded() == True, 'Search results page did not load.'
    print(f"\nSearch page loaded successfully - {searchproduct}.")


@pytest.mark.parametrize("searchproduct", [
    ("wireless mouse"), ("shoes")
])
def test_find_elements_amazon(driver, searchproduct):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Search Product - {searchproduct}")
    homepage.click_search_button()
    print()

    assert homepage.is_amazon_page_loaded() == True, 'Search results page did not load.'
    print(f"\nSearch page loaded successfully - {searchproduct}.")

    productlistpage = ProductListPage(driver)

    productlistpage.first_product_title()
    value = productlistpage.all_products()

    assert value, "No products found on Amazon search results."


@pytest.mark.parametrize(("searchproduct", "brandname"), [
    ("wireless mouse", "Logitech"),
    ("shoes", "Nike")
])
def test_brand_filter(driver, searchproduct, brandname):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Search Product - {searchproduct}")
    homepage.click_search_button()
    print()

    assert homepage.is_amazon_page_loaded() == True, 'Search results page did not load.'
    print(f"\nSearch page loaded successfully - {searchproduct}.")

    productlistpage = ProductListPage(driver)

    productlistpage.select_brand_filter(brandname)

    assert productlistpage.check_product_titles_for_brand_filter(brandname), "Brand filter did not apply properly."






