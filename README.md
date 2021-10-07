# BDD-Framework


BDD framework Skeleton from scratch

This is an attempt to create a simple BDD framework which is ready to use with any webapp.
There are many things pending but as part of Hackathon at Qxf2 in ~10hours I could build this and it work !!!

Directory structure
 For BDD if you google you will see this generic directory structure. 

[project root directory]
|‐‐ [product code packages]
|-- [test directories]
|   |-- features
|   |   `-- *.feature
|   `-- step_defs
|       |-- __init__.py
|       |-- conftest.py
|       `-- test_*.py
`-- [pytest.ini|tox.ini|setup.cfg]

I am trying to follow more or less the same structure but with modifications to suite my needs.

There are essentially there parts to my directory
Tests folder
Where actual tests are written
Tests are further divided onto - Frontend, backend, API - to group our tests
Utlis
It contains the common methods /functions needed to run my tests
This will be growing as the framework grows. Currently it has 3 parts
CommonConfigs
Thing like URL, locators are stored here
Commonwebsteps
Common webelement steps are written here
Commonweb
These are actual python selenium wrappers
Under Tests/Specific Module steps - these are not common and may not be reused hence can be written here. This can be visualised as Page wise tests which are specific to page. It can use framework steps also.

Tests can be executed using many parameters to behave commands, simply running behave command on tests folder will execute all tests one after the other. Recommended way is to have tags in your tests/scenarios and use them to run tests

Basic report can be generated using json command

Currently repo shows 3 test examples which show to write reusable tests using simple scenario and scenario outline.

Steps to create Feature > corresponding step definition and add selenium wrapper 
Create test under Tests folder with filename suffixed with .feature
Try to write generic step e.g “Given I go to "Factorial app" page
Here the page name can be different but action to happen at the backend will be same Hence we can write this in generic step file
If the step is not generic try to group them under folder which server similar purpose
Step definition will ideally call a python function which will serve as wrapper to webelement actions. So we can add them into utility.
Again when adding to utility try to see if it can be generic enough to be kept as common one 


	



Further plan 
Not able to make environment.py working
Runner related things needs to check
Running tests on docker
CICD 
