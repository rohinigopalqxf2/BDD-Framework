from selenium import webdriver


def go_to(url, browser_type=None):
    """
    Functions to start instance of browser and open the url
    :param url:
    :param browser_type:
    :return:
    """
    # url is coming as "https/google.com", symbol " is causing browser to fail.
    url = url.strip('"')
    if not browser_type:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get(url)

    else:
        raise Exception("The browser type '{}' is not supported".format(browser_type))

    # clean the url and go to url
    driver.get(url)

    return driver


def assert_page_title(context, expected_title):
    """
    Function to asset page title
    :param context:
    :param expected_title:
    :return:
    """
    actual_title = context.driver.title
    # expected_title = expected_title.strip('"')
    assert expected_title == actual_title, "The title is not expected" \
                                           "Expected : {}, Actual : {}".format(expected_title, actual_title)


def assert_page_url(context, expected_url):
    """
    Function to assert page url
    :param context:
    :param expected_url:
    :return:
    """

    current_url = context.driver.getCurrentUrl()
    if not expected_url.startswith('http://') or not expected_url.startswith('https://'):
        expected_url = "https://" + expected_url + "/"

    assert current_url == expected_url, "The URL mismatch" \
                                        "Expected URL : {}, Actual URL : {}".format(expected_url, current_url)


def find_element(context, locator_attrib, locator_text):
    """
    Find element and returns the obj
    :param context:
    :param locator_attrib:
    :param locator_text:
    :return:
    """
    possible_locators = ["id", "css selector", "xpath", "name", "tag name", "class"]

    if locator_attrib not in possible_locators:
        raise Exception("Locator element is not present in possible locator list")
    try:
        element = context.driver.find_element(locator_attrib, locator_text)
        return element
    except Exception as e:
        raise Exception(e)


def if_element_visible(element):
    """
    Finds if element is visible
    :param context:
    :return:
    """
    if element.is_displayed():
        return True
    else:
        return False


def type_into_element(context_or_element, input_value, locator_attrib, locator_text):
    """
    Function to insert values to textboxes

    :param context_or_element:
    :param input_value:
    :param locator_attrib:
    :param locator_text:
    :return:
    """
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        input_field = context_or_element
    else:
        input_field = context_or_element.driver.find_element(locator_attrib, locator_text)
    input_field.send_keys(input_value)


def click(context_or_element, locator_attrib, locator_text):
    """
    Fucntion to perform click event on elements [Tested for buttom]
    :param context_or_element: 
    :param locator_attrib: 
    :param locator_text: 
    :return: 
    """
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_attrib, locator_text)

    element.click()


def element_contains_text(context_or_element, expected_text, locator_attrib, locator_text, case_sensitive=True):
    """

    :param expected_text:
    :param case_sensitive:
    :param context_or_element:
    :param locator_attrib:
    :param locator_text:
    :return:
    """
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_attrib, locator_text)

    element_text = element.text
    if not case_sensitive:
        if expected_text.lower() in element_text.lower:
            return True
        else:
            return False
    else:
        return True if expected_text in element_text else False
