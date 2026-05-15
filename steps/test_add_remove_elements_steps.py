from pytest_bdd import given, parsers, scenarios, then, when

from pages.add_remove_elements_page import AddRemoveElementsPage

scenarios("../features/add_remove_elements.feature")


@given("the user opens the add remove elements page", target_fixture="current_page")
def open_add_remove_elements_page(unauthenticated_page):
    page = AddRemoveElementsPage(unauthenticated_page)
    page.open()
    return unauthenticated_page


@given(parsers.parse("the user adds {count:d} dynamic elements"))
def add_dynamic_elements_given(current_page, count):
    AddRemoveElementsPage(current_page).add_elements(count)


@when(parsers.parse("the user adds {count:d} dynamic elements"))
def add_dynamic_elements_when(current_page, count):
    AddRemoveElementsPage(current_page).add_elements(count)


@when(parsers.parse("the user removes {count:d} dynamic element"))
def remove_dynamic_elements(current_page, count):
    AddRemoveElementsPage(current_page).remove_elements(count)


@then(parsers.parse("{count:d} delete controls are visible"))
def delete_controls_visible_plural(current_page, count):
    AddRemoveElementsPage(current_page).expect_delete_count(count)


@then(parsers.parse("{count:d} delete control is visible"))
def delete_controls_visible_singular(current_page, count):
    AddRemoveElementsPage(current_page).expect_delete_count(count)
