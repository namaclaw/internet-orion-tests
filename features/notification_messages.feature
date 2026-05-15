Feature: Notification Messages
  Rendered notifications should be visible without relying on exact randomized copy.

  Scenario: A rendered notification banner becomes visible
    Given the user opens the notification messages page
    When the user requests a new notification message
    Then the notification banner is visible
    And the notification message belongs to the allowed message family
