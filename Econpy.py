#!/usr/bin/python3.6

# Site trying to scrape: http://econpy.pythonanywhere.com/ex/001.html

import traceback
from selenium import webdriver


# Firefox will run in a virtual display, that you will not see the browser
browser = webdriver.Firefox()
browser.get('http://econpy.pythonanywhere.com/ex/001.html')


try:
    assert 'Items 1 to 20 -- Example Page 1' in browser.title
except AssertionError as e:
    print("Oops, went to the wrong place!:", traceback.format_exc())

print(browser.title)

# el.text for el finds the text elements for the elements found in the xpath
# Source that helped me make it work
# https://stackoverflow.com/questions/43926155/how-to-get-text-content-of-multiple-elements-with-python-selenium
names = [el.text for el in browser.find_elements_by_xpath("/html/body/div/div")]
price = [el.text for el in browser.find_elements_by_xpath("/html/body/div/span")]
# Joins the 2 lists together
combined_list = ([": ".join(pair) for pair in zip(names, price)])
# Separates each joined pair with a new line and stores it in
final = '\n'.join(combined_list)
print(final)

# Just cleaning up by closing the browser
browser.quit()


