import pytest
from pages.home_page import HomePage
from pages.product_listing_page import ProductListPage


@pytest.mark.parametrize(("searchproduct", "brandname", "mensize"), [
    ("shoes", "Nike", "9")
])
def test_product_ordering(driver, searchproduct, brandname, mensize):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Search Product - {searchproduct}")
    homepage.click_search_button()
    print()

    assert homepage.is_amazon_page_loaded() == True, 'Search results page did not load.'
    print(f"\nSearch page loaded successfully - {searchproduct}.")

    productlistpage = ProductListPage(driver)

    productlistpage.select_brand_filter(brandname)
    print(f"\nApplying Brand Filter - {brandname}.")

    assert productlistpage.check_product_titles_for_brand_filter(brandname), "Brand filter did not apply properly."

    productlistpage.men_size_locator(mensize)
    print(f"\nApplying size Filter - {mensize}.")

    assert productlistpage.check_size(mensize), "Size filter did not applied.."
