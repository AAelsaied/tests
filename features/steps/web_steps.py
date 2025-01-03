@when('I click the button "{button_name}"')
def step_impl(context, button_name):
    context.driver.find_element_by_name(button_name).click()

@then('I should see the text "{text}"')
def step_impl(context, text):
    assert text in context.driver.page_source

@then('I should not see the text "{text}"')
def step_impl(context, text):
    assert text not in context.driver.page_source

@then('I should see the message "{message}"')
def step_impl(context, message):
    assert message in context.driver.page_source

