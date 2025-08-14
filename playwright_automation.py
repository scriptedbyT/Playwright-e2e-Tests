from playwright.sync_api import Playwright, sync_playwright, expect
import re
import os
import multiprocessing
import pandas as pd
from time import sleep, perf_counter

url = 'https://demoqa.com/'
opt1_url = url + 'elements'
opt2_url = url + 'automation-practice-form'
opt3_url = url + 'interaction'

def run(playwright: Playwright) -> None:
    # Browser [Chrome, Firefox, WebKit]
    # browser = playwright.firefox.lanch(headless=False)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    sleep(2)

    # Website Menu
    print("---- Tools QA Menu ----")
    print('\n')
    print("1 - Elements")
    print("2 - Forms")
    print("3 - Interactions")
    print('\n')


    n = input('Enter your option for further navigations:')
    opt = str(n)

    if opt == '1':
        # print("1 - Elements")
        page.goto(opt1_url)
        sleep(2)

        ## ---- Text Box ---- ##
        page.goto(url + 'text-box')
        sleep(0.5)
        page.locator('//input[@id="userName"]').fill('pl_user')
        sleep(0.2)
        page.locator('//input[@id="userEmail"]').fill('pl_user@user.com')
        sleep(0.2)
        page.locator('//textarea[@id="currentAddress"]').click()
        page.keyboard.type('rich text testinggg. This is simple sentence in text box...')
        sleep(1)
        page.locator('//textarea[@id="permanentAddress"]').click()
        page.keyboard.type('rich text testinggg. This is simple sentence in text box...')
        sleep(1)
        page.screenshot()
        page.locator('//button[@id="submit"]').click()
        sleep(2)
        print("Text Box Section finished!")

        
        ## ---- Checkbox ---- ##
        sleep(2)
        page.goto(url + 'checkbox')
        
        # Expand All
        page.locator('//button[@title="Expand all"]').click()

        # Check All
        # page.locator('//span[text()="Home"]/ancestor::label//input[@id="tree-node-home"]').check()
        # page.locator('//span[text()="Home"]/ancestor::label//input[@id="tree-node-home"]').uncheck()
        page.locator('//span[text()="Home"]').click()
        sleep(1)
        page.locator('//span[text()="Public"]').click()
        sleep(1)
        page.locator('//span[text()="Classified"]').click()
        sleep(1)
        # page.video()
        # page.screenshot()
        print('Checkbox Section finished!')
        sleep(2)


        ## ---- Radio Button ---- ##
        page.goto(url + 'radio-button')
        sleep(1)
        page.locator('//div//label[@for="impressiveRadio"]').click()
        sleep(2)


        ## ---- Web Tables ---- ##
        page.goto(url + 'webtables')
        sleep(2)

        # Listing view set  
        page.locator('//span[contains(@class,"select-wrap")]').scroll_into_view_if_needed()
        page.locator('//span[contains(@class,"select-wrap")]//select').select_option('100 rows')
        sleep(2)     
        # Accessing Table - 
        # //tbody//tr//td [Table body, row, data]
         
        # Edit Value
        page.locator('(//div[@class="action-buttons"])[2]//span[@title="Edit"]').click()
        sleep(1)
        # If data is required for modifications - edit here
        page.locator('//button[@id="submit"]').click()

        # Delete Value
        page.locator('(//div[@class="action-buttons"])[2]//span[@title="Delete"]').scroll_into_view_if_needed()
        page.locator('(//div[@class="action-buttons"])[2]//span[@title="Delete"]').click()
        sleep(2)

        # Add Value
        page.locator('//button[text()="Add"]').click()
        sleep(1)
        # Basic Information
        page.locator('//input[@placeholder="First Name"]').fill('name1')
        sleep(0.2)
        page.locator('//input[@placeholder="Last Name"]').fill('name2')
        sleep(0.2)
        page.locator('//input[@id="userEmail"]').fill('name1@example.com')
        sleep(0.2)
        page.locator('//input[@placeholder="Age"]').fill('25')
        sleep(0.2)
        page.locator('//input[@placeholder="Salary"]').fill('100000')
        sleep(0.2)
        page.locator('//input[@placeholder="Department"]').fill('IT Sector')
        sleep(1)
        page.locator('//button[@id="submit"]').click()
        sleep(2)
        print('WebTables Section finished!')


        ## ---- Buttons ---- ##
        page.goto(url + 'buttons')
        sleep(1)
        # Double Click
        page.locator('//button[@id="doubleClickBtn"]').dblclick()
        sleep(1)
        # Right Click
        page.locator('//button[@id="rightClickBtn"]').click(button='right')
        sleep(1)
        # Click
        page.locator('//button[text()="Click Me"]').click()
        sleep(2)
        print('Button Section finished!')


        ## ---- Download & Upload ---- ##
        page.goto(url + 'upload-download')
        sleep(1)

        # Download
        with page.expect_download() as download_info:
            page.locator('//a[text()="Download"]').click()
        download = download_info.value
        # print(download)
        # print(download.path())

        folder_path = '/Users/taneshkamehta/Documents/RPA/Playwright/Fundamentals/ '

        # Downloading on Required PATH
        #  download.save_as('PATH' + download.suggested_filename)
        download.save_as(folder_path + download.suggested_filename)
        sleep(2)

        # # Upload
        fl_path = '/Users/taneshkamehta/Documents/RPA/Playwright/Fundamentals/ sampleFile.jpeg'
        page.locator('//input[@type="file"]').set_input_files(str(fl_path))
        sleep(2)
        print('Download-Upload Section finished!')


        ## ---- Download & Upload ---- ##        
        page.goto(url + 'dynamic-properties')
        sleep(1)
        page.locator('//button[@id="enableAfter"]').hover()
        sleep(6)
        print('Dynamic Section finished!')


    elif opt == '2':
        # print("2 - Forms")
        page.goto(opt2_url)
        sleep(2)

        # Registration Form
        # Name
        page.locator('//input[@placeholder="First Name"]').fill('firstname')
        sleep(0.2)
        page.locator('//input[@placeholder="Last Name"]').fill('lastname')
        #Email
        page.locator('//input[@id="userEmail"]').fill('user@gmail.com')
        sleep(0.2)
        #Gender
        page.locator('//input[@name="gender"]/following::label[text()="Female"]').click()
        # Mobile Number
        page.locator('//input[@placeholder="Mobile Number"]').fill('9999999999')
        sleep(0.1)
        # Date of Birth
        page.locator('//input[@id="dateOfBirthInput"]').click()
        page.locator('//div//select[contains(@class, "__year-select")]').select_option('2001')
        sleep(0.2)
        page.locator('//div//select[contains(@class, "__month-select")]').select_option('April')
        sleep(0.2)
        page.locator('//div[contains(@class, "react-datepicker") and text()="24"]').click()
        sleep(2)
        # Subjects
        page.locator('//input[@id="subjectsInput"]').fill('Maths, English, Science, Hindi, German')
        sleep(0.2)
        # Hobbies
        page.locator('//label[@for="hobbies-checkbox-1"]').click()
        page.locator('//label[@for="hobbies-checkbox-2"]').click()
        page.locator('//label[@for="hobbies-checkbox-3"]').click()
        sleep(1)
        # Picture
        fl_path = '/Users/taneshkamehta/Documents/RPA/Playwright/Fundamentals/ sampleFile.jpeg'
        page.locator('//input[@type="file"]').set_input_files(fl_path)
        sleep(1)
        # Current Address
        page.locator('//textarea').click()
        page.keyboard.type('West Delhi, New Delhi, 110027, Delhi, India')
        sleep(2)
        # State and City
        page.locator('//div[@id="state"]').click()
        sleep(0.4)
        page.locator('//div[@id="state"]//input').fill('NCR')
        page.keyboard.press('Enter')
        sleep(2)

        page.locator('//div[@id="city"]').click()
        sleep(0.4)
        page.locator('//div[@id="city"]//input').fill('Delhi')
        page.keyboard.press('Enter')
        sleep(2)

        # Submit Form
        page.locator('//button[@id="submit"]')
        sleep(4)
        print('Registration Form Submitted!!')

    
    elif opt == '3':
        # print("3 - Interactions")
        page.goto(opt3_url)
        sleep(2)

        # Sorting [Drag and Drop]
        page.goto('https://demoqa.com/sortable')
        sleep(1)

        # Grid Sorting
        page.locator('//a[text()="Grid"]').click()
        sleep(2)
        page.locator('(//div[text()="Three"])[2]').drag_to(page.locator('(//div[text()="One"])[2]'))
        sleep(2)
        page.locator('(//div[text()="Seven"])[1]').drag_to(page.locator('(//div[text()="Nine"])[1]'))
        sleep(2)

        # List Sorting
        page.locator('//a[text()="List"]').click()
        sleep(2)
        page.locator('(//div[text()="One"])[1]').drag_to(page.locator('(//div[text()="Four"])[1]'))
        sleep(2)
        page.locator('(//div[text()="Six"])[1]').drag_to(page.locator('(//div[text()="Two"])[1]'))
        sleep(2)


    context.close()
    browser.close()


def fn_run():
    # information('function f')
    with sync_playwright() as playwright:
        run(playwright)

if __name__ == "__main__":
    start = perf_counter()
    fn_run()
    end = perf_counter()
    print(f'\n---------------\n Finished in {round(end-start, 2)} second(s)')
