# Created by RohiniGopal at 07-10-2021
@regression
Feature: Verify the Factorial app

  Scenario: Verify Factorial app functionality
    Given I go to "Factorial app" page
    Then  the page title should be "Factoriall"
    Then I type "123" in the name field in Factorial text
    And I click on "Calculate" button