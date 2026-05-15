Feature: Add Remove Elements
  Dynamically added controls should be visible and removable.

  Scenario: Adding elements creates one delete control per click
    Given the user opens the add remove elements page
    When the user adds 2 dynamic elements
    Then 2 delete controls are visible

  Scenario: Removing an element hides the clicked delete control
    Given the user opens the add remove elements page
    And the user adds 2 dynamic elements
    When the user removes 1 dynamic element
    Then 1 delete control is visible
