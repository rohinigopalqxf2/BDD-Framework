
from behave import given, then
from Utils.CommonFunctions import webcommon
from Utils.CommonConfigs import  AppURLConfigs


@given('I go to {site} page')
def go_to_url(context, site):
    """
    Step defination to go and open a url
    :param context:
    :param site:
    :return:
    """
    site_new = site.strip('"')
    url = AppURLConfigs.URL.get(site_new)
    context.driver = webcommon.go_to(url)


@then('the page title should be "{expected_title}"')
def verify_page_title(context, expected_title):
    """
    Verifies the page title
    :param context:
    :param expected_title:
    :return:
    """
    webcommon.assert_page_title(context, expected_title)

