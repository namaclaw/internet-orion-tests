Feature: JavaScript Alerts
  Result banners should reflect the handled browser dialog action.

  Scenario: Accepting a JavaScript alert updates the result
    Given the user opens the JavaScript alerts page
    When the user accepts the JavaScript alert
    Then the JavaScript alerts result shows "You successfully clicked an alert"

  Scenario: Dismissing a JavaScript confirm updates the result
    Given the user opens the JavaScript alerts page
    When the user dismisses the JavaScript confirm
    Then the JavaScript alerts result shows "You clicked: Cancel"

  Scenario: Submitting text to a JavaScript prompt updates the result
    Given the user opens the JavaScript alerts page
    When the user submits "Orion prompt" to the JavaScript prompt
    Then the JavaScript alerts result shows "You entered: Orion prompt"
