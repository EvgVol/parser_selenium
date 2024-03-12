# parser_selenium

## Installation
To install and run the project locally, follow these steps:

1. Clone the repository using:
```
git clone https://github.com/EvgVol/parser_selenium.git
```
2. Navigate to the project directory using:
```
cd evosoft
```
3. Create and install of virtual environments by executing the command:
```
poetry install
```
4.  Start test_parser.py for Chrome using the following command:
```
poetry run pytest evosoft/tests/test_parser.py
```
5.  Start test_user_simulation.py for Chrome using the following command:
```
poetry run pytest evosoft/tests/test_user_simulation.py
```
6. You can also run the tests using the following command:
```
poetry run pytest
```

**First make sure that you have registered and added chromedriver to the PATH**

*You can also run tests for the firefox browser by downloading the appropriate driver.*

*p.s. Don't forget to update your `coftest.py`*