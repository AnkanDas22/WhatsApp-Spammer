from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

x=input('Press any key after scanning QR code to login')

while True:
    try:
        name = input('Name of the user or the group : ')
        msg = input('Put your message here : ')
        count = int(input('Number of times you want to send the same message : '))

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        msg_box = driver.find_element_by_class_name('input-container')

        for i in range(count):
            msg_box.send_keys(msg)
            driver.find_element_by_class_name('compose-btn-send').click()
    except:
        print("Sorry nothing was found by that name.\n")
    choice=input("Do you want to continue?\n1-> YES\tAnything else->NO\n")
    if '1' in choice:
        pass
    else:
        break

x=input("Don't do anything that harms the experience of other users.\nUse at your own risk\nPress Enter to exit...")
