from behave import step
from Utils.CommonFunctions import webcommon
from Utils.CommonConfigs import FactorialAppConfig

@step('I type "{value}" in the name field in Factorial text')
def enter_value(context, value):
    name_locator_attrib = FactorialAppConfig.FACTORIAL['input_field']['type']
    name_locator_string = FactorialAppConfig.FACTORIAL['input_field']['locator']
    webcommon.type_into_element(context, value, name_locator_attrib, name_locator_string)

@step('I click on "{calc_bt}" button')
def bt_click(context, calc_bt):
    calc_locator_attrib = FactorialAppConfig.FACTORIAL['calc_button']['type']
    calc_locator_string = FactorialAppConfig.FACTORIAL['calc_button']['locator']
    webcommon.click(context, calc_locator_attrib, calc_locator_string)