# Created by RohiniGopal at 07-10-2021
Feature: Verify the Example form on Selenium main tutorials page

  @smoke
  Scenario: Verify Example form functionality
    Given I go to "tutorials" page
    Then  the page title should be "Qxf2 Services: Selenium training main"
    Then I type "Rohini1" in the name field in Example Form
    Then I type "ro@ro.com" in the email field in Example Form
    Then I type "99002321" in the phone field in Example Form
    And click on "Click me" button


  Scenario:Verify error message when invalid email is entered
    Given I go to "tutorials" page
    Then  the page title should be "Qxf2 Services: Selenium training main"
    Then I type "Rohini2" in the name field in Example Form
    Then I type "rohini2" in the email field in Example Form
    Then I type "99002321" in the phone field in Example Form
    And click on "Click me" button
    Then error message "Please enter a valid email address" should be displayed
