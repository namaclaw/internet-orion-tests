from pytest_bdd import given, scenarios, then, when

from pages.dynamic_loading_page import DynamicLoadingPage

scenarios("../features/dynamic_loading.feature")


@given("the user opens the dynamic loading example 1 page", target_fixture="current_page")
def open_dynamic_loading_example_1(unauthenticated_page):
    DynamicLoadingPage(unauthenticated_page, "/dynamic_loading/1").open()
    return unauthenticated_page


@given("the user opens the dynamic loading example 2 page", target_fixture="current_page")
def open_dynamic_loading_example_2(unauthenticated_page):
    DynamicLoadingPage(unauthenticated_page, "/dynamic_loading/2").open()
    return unauthenticated_page


@when("the user starts dynamic loading example 1")
def start_dynamic_loading_example_1(current_page):
    DynamicLoadingPage(current_page, "/dynamic_loading/1").start()


@when("the user starts dynamic loading example 2")
def start_dynamic_loading_example_2(current_page):
    DynamicLoadingPage(current_page, "/dynamic_loading/2").start()


@then("the loading indicator disappears for dynamic loading example 1")
def loading_indicator_disappears_example_1(current_page):
    DynamicLoadingPage(current_page, "/dynamic_loading/1").wait_for_loading_to_finish()


@then("the loading indicator disappears for dynamic loading example 2")
def loading_indicator_disappears_example_2(current_page):
    DynamicLoadingPage(current_page, "/dynamic_loading/2").wait_for_loading_to_finish()


@then("the revealed hello world message is visible for dynamic loading example 1")
def hello_world_visible_example_1(current_page):
    DynamicLoadingPage(current_page, "/dynamic_loading/1").expect_finish_visible()


@then("the revealed hello world message is visible for dynamic loading example 2")
def hello_world_visible_example_2(current_page):
    DynamicLoadingPage(current_page, "/dynamic_loading/2").expect_finish_visible()
