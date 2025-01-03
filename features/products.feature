Scenario: Reading a product
    Given there are some products
    When I visit the "Product A" page
    Then I should see the product details


Scenario: Updating a product
    Given I have a product "Product A"
    When I update the product's name to "Updated Product A"
    Then the product name should be "Updated Product A"

Scenario: Updating a product
    Given I have a product "Product A"
    When I update the product's name to "Updated Product A"
    Then the product name should be "Updated Product A"

Scenario: Deleting a product
    Given I have a product "Product A"
    When I delete the product
    Then the product should no longer exist

Scenario: Listing all products
    Given there are some products
    When I view the list of products
    Then I should see all products

Scenario: Searching by category
    Given there are products in "Category 1"
    When I search for "Category 1"
    Then I should see all products in "Category 1"


Scenario: Searching by availability
    Given there are available and unavailable products
    When I search for available products
    Then I should see only available products

Scenario: Searching by name
    Given there are products with names "Product A" and "Product B"
    When I search for "Product A"
    Then I should see "Product A"
