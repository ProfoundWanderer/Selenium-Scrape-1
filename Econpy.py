#!/usr/bin/python3.6


from selenium import webdriver
import csv


# Firefox will run in a virtual display, that you will not see the browser
browser = webdriver.Firefox()
urls = [
    'http://econpy.pythonanywhere.com/ex/001.html',
    'http://econpy.pythonanywhere.com/ex/002.html',
    'http://econpy.pythonanywhere.com/ex/003.html',
    'http://econpy.pythonanywhere.com/ex/004.html',
    'http://econpy.pythonanywhere.com/ex/005.html'
]

for url in urls:
    browser.get(url)

    # print(browser.title) in case you want to see which page it is on
    # may have to add explicit wait here if issues arise with page loading

    # el.text for el finds the text elements for the elements found in the xpath
    name = [el.text for el in browser.find_elements_by_xpath("/html/body/div/div")]
    price = [el.text for el in browser.find_elements_by_xpath("/html/body/div/span")]

    # Creates csv file and sets it to be written to
    with open('NamesAndPrices.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        # Goes through and prints the name and price in sepearate columns on a row
        # then keeps doing that on each row until all names and prices are outputted
        for row in zip(name, price):
            writer.writerow(row)

    # Below comments are in case you wanted to print the results out to terminal

    # Joins the 2 lists together
    # combined_list = ([": ".join(pair) for pair in zip(name, price)])

    # Separates each joined pair with a new line and stores it in
    # final = '\n'.join(combined_list)
    # print(final)

# Just cleaning up by closing the browser and virtual display
browser.quit()
