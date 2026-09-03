# PRODIGY_ST_03 – Automated Login Testing

## Objective

To automate and test the login functionality of the SauceDemo website using Selenium WebDriver with Python.

## Website Tested

SauceDemo
https://www.saucedemo.com/

## Tools Used

* Python
* Selenium WebDriver
* Google Chrome
* VS Code

## Test Cases

| Test Case | Description                   | Expected Result                         | Status |
| --------- | ----------------------------- | --------------------------------------- | ------ |
| TC01      | Valid username and password   | User successfully logs in               | PASS   |
| TC02      | Invalid username and password | Login is rejected with an error message | PASS   |
| TC03      | Empty username                | Username required message is displayed  | PASS   |
| TC04      | Empty password                | Password required message is displayed  | PASS   |
| TC05      | Locked-out user               | Locked-out error message is displayed   | PASS   |

## Test Accounts

### Valid User

* Username: `standard_user`
* Password: `secret_sauce`

### Locked-out User

* Username: `locked_out_user`
* Password: `secret_sauce`

## Conclusion

All five automated login test cases were successfully executed using Selenium WebDriver. The SauceDemo login functionality behaved as expected for valid, invalid, empty-field, and locked-out user scenarios.

