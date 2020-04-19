# Automate_Login

## Facebook

Login to facebook through terminal

To run the script clone the repository 
```
git clone https://github.com/hemant-taneja/Automate_Login.git
```

and write in the cmd/powershell/terminal
```
python login.py "your email address" "your password"
```

NOTE: Quotation marks are not to be used
Go through the documentation for the setup of selenium https://selenium-python.readthedocs.io/
Using Virtual Environment is recommended

## Github

Changes in the code
```
username = browser.find_element_by_name("login")
password = browser.find_element_by_name("password")
submit   = browser.find_element_by_name("commit")
```
