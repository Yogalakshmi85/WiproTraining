
  Feature: Search

   Scenario: Search for product with results
     Given buyer is on the olx homepage
     When buyer types product in searchbar
     Then search results should be displayed

#   Scenario: Search for a product with no results
#     Given buyer is on the olx homepage
#     When buyer types product in searchbar
#     Then error message should be displayed

