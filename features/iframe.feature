Feature: iFrame editor
  The TinyMCE editor should remain reachable through its iframe.

  Scenario: The TinyMCE editor chrome and body are visible
    Given the user opens the iframe page
    Then the TinyMCE toolbar is visible
    And the TinyMCE editor body is visible

  Scenario: The TinyMCE editor body text can be replaced
    Given the user opens the iframe page
    When the user replaces the TinyMCE body text with "Edited by Orion"
    Then the TinyMCE editor body shows "Edited by Orion"
