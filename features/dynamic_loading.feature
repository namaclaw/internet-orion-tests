Feature: Dynamic Loading
  Explicit waits should reveal dynamically loaded content without brittle sleeps.

  Scenario: Example 1 reveals the hidden element after loading completes
    Given the user opens the dynamic loading example 1 page
    When the user starts dynamic loading example 1
    Then the loading indicator disappears for dynamic loading example 1
    And the revealed hello world message is visible for dynamic loading example 1

  Scenario: Example 2 renders the hidden element after loading completes
    Given the user opens the dynamic loading example 2 page
    When the user starts dynamic loading example 2
    Then the loading indicator disappears for dynamic loading example 2
    And the revealed hello world message is visible for dynamic loading example 2
