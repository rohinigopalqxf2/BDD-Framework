
from behave import step
from Utils.CommonFunctions import webcommon
from Utils.CommonConfigs import SeleniumTutorialConfig

@step('I type "{name}" in the name field in Example Form')
def enter_name(context, name):
    name_locator_attrib = SeleniumTutorialConfig.EXAMPLE_FORM['name']['type']
    name_locator_string = SeleniumTutorialConfig.EXAMPLE_FORM['name']['locator']
    webcommon.type_into_element(context, name, name_locator_attrib, name_locator_string)


@step('I type "{email}" in the email field in Example Form')
def enter_email(context, email):
    email_locator_attrib = SeleniumTutorialConfig.EXAMPLE_FORM['email']['type']
    email_locator_string = SeleniumTutorialConfig.EXAMPLE_FORM['email']['locator']
    webcommon.type_into_element(context, email, email_locator_attrib, email_locator_string)

@step('I type "{phone}" in the phone field in Example Form')
def enter_phone(context, phone):
    phone_locator_attrib = SeleniumTutorialConfig.EXAMPLE_FORM['phone']['type']
    phone_locator_string = SeleniumTutorialConfig.EXAMPLE_FORM['phone']['locator']
    webcommon.type_into_element(context, phone, phone_locator_attrib, phone_locator_string)

@step('click on "{button}" button')
def click_me(context, button):
    bt_locator_attrib = SeleniumTutorialConfig.EXAMPLE_FORM['click_me_button']['type']
    bt_locator_string = SeleniumTutorialConfig.EXAMPLE_FORM['click_me_button']['locator']
    webcommon.click(context, bt_locator_attrib, bt_locator_string)
    #webcommon.assert_page_title(context, "Qxf2 Services: Selenium training redirect")

@step('error message "{expected_message}" should be displayed')
def assert_error(context, expected_message):
    error_message_type = SeleniumTutorialConfig.EXAMPLE_FORM['error_message']['type']
    error_message_string = SeleniumTutorialConfig.EXAMPLE_FORM['error_message']['locator']

    webcommon.element_contains_text(context, expected_message, error_message_type, error_message_string)