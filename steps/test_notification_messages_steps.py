from pytest_bdd import given, scenarios, then, when

from pages.notification_messages_page import NotificationMessagesPage

scenarios("../features/notification_messages.feature")


@given("the user opens the notification messages page", target_fixture="current_page")
def open_notification_messages_page(unauthenticated_page):
    page = NotificationMessagesPage(unauthenticated_page)
    page.open()
    return unauthenticated_page


@when("the user requests a new notification message")
def request_new_notification_message(current_page):
    NotificationMessagesPage(current_page).request_new_message()


@then("the notification banner is visible")
def notification_banner_visible(current_page):
    NotificationMessagesPage(current_page).expect_banner_visible()


@then("the notification message belongs to the allowed message family")
def notification_message_allowed_family(current_page):
    NotificationMessagesPage(current_page).expect_allowed_message_family()
