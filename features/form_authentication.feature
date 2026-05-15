Feature: Form Authentication
  The Internet demo auth flow should preserve clear unauthenticated and authenticated behavior.

  Scenario: Successful login redirects to the secure area
    Given the user opens the login page
    When the user signs in with valid public demo credentials
    Then the secure area is displayed
    And a success flash message is shown

  Scenario: Logout returns the user to the login page
    Given the user is signed in on the secure area
    When the user logs out
    Then the login page is displayed again
    And a logout flash message is shown

  Scenario: Invalid username is rejected
    Given the user opens the login page
    When the user signs in with an invalid username
    Then the login page remains displayed
    And an invalid username flash message is shown

  Scenario: Invalid password is rejected
    Given the user opens the login page
    When the user signs in with an invalid password
    Then the login page remains displayed
    And an invalid password flash message is shown

  Scenario: Empty credentials are rejected
    Given the user opens the login page
    When the user submits the login form with empty fields
    Then the login page remains displayed
    And an invalid username flash message is shown

  Scenario: Direct secure-area access before login redirects to login
    Given the user is unauthenticated
    When the user opens the secure area directly
    Then the login page is displayed again
    And an authentication-required flash message is shown

  Scenario: Direct secure-area access after login keeps the session active
    Given the user has an authenticated browser state
    When the user opens the secure area directly from authenticated state
    Then the secure area is displayed
    And the logout control is available

  Scenario: Flash message is visible after a successful login
    Given the user opens the login page
    When the user signs in with valid public demo credentials
    Then a success flash message is shown
    And the flash message is visible

  Scenario: Flash message is visible after a failed login
    Given the user opens the login page
    When the user signs in with an invalid password
    Then an invalid password flash message is shown
    And the flash message is visible
