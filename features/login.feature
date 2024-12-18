Feature: End-to-End Checkout on SauceDemo

  Scenario: Login, add two products to cart, checkout, and verify success message
    Given I open the SauceDemo website
    When I login with "standard_user" and "secret_sauce"
    And I add "sauce-labs-backpack" and "sauce-labs-bike-light" to the cart
    And I proceed to checkout and fill the form with "John", "Doe", and "12345"
    Then I should see "Thank you for your order!" on the confirmation page