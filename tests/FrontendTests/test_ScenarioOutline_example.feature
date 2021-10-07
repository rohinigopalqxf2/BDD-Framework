# Created by RohiniGopal at 07-10-2021
Feature: Showing useage of scenario outline

  Scenario Outline: Verify Example form functionality
    Given I go to "<URL>" page
    Then  the page title should be "<title>"

    Examples:
        |URL            | title                                |
        | tutorials     | Qxf2 Services: Selenium training main|
        | Factorial app | Factoriall                           |
