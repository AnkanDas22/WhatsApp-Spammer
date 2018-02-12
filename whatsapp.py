from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

x=input('Press any key after scanning QR code to login')

while True:
    try:
        choice=int(input("Single user spam?-1\nMultiple user spam?-2\nAll user spam-3\n\n"))
        if(choice==1):
            name = input('Name of the user or the group : ')
            msg = input('Put your message here : ')
            count = int(input('Number of times you want to send the same message : '))
            
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()
            time.sleep(1)
            msg_box = driver.find_element_by_xpath('//div[@class="pluggable-input-body copyable-text selectable-text"]')
            for i in range(count):
                msg_box.send_keys(msg)
                try:
                    driver.find_element_by_xpath('//span[@data-icon="send"]').click()
                except:
                    driver.find_element_by_xpath('//button[@class="_2lkdt"]').click()
                
        elif(choice==2):
            listx=[]
            print('Remember:- Input stream will only be stopped when you input -1 as username')
            while True:
                names=input("Enter name of user or group\n")
                listx.append(names)
                try:
                    if(int(names)==-1):
                        break
                except:
                    pass
            msgx=input("Put your message here : ")
            countx=int(input("Number of times you want to send the same message : "))
            for i in listx:
                userx = driver.find_element_by_xpath('//span[@title = "{}"]'.format(i))
                userx.click()
                msg_boxx = driver.find_element_by_xpath('//div[@class="pluggable-input-body copyable-text selectable-text"]')
                time.sleep(1)
                for j in range(countx):
                    msg_boxx.send_keys(msgx)
                    try:
                        driver.find_element_by_xpath('//button[@class="_2lkdt"]').click()
                    except:
                        driver.find_element_by_xpath('//span[@data-icon="send"]').click()
            listx.clear()

        elif(choice==3):
            cho=input("Are you sure you want to send messages to all users in your contacts?\n1-> YES, 2-> NO\n")
            if(int(cho)==1):
                msgz=input("Put your message here : ")
                countz=int(input("Number of times you want to send the same message : "))
                userx = driver.find_elements_by_xpath('//span[@class="_1wjpf"]')
                for i in userx:
                    i.click()
                    msg_boxz = driver.find_element_by_xpath('//div[@class="pluggable-input-body copyable-text selectable-text"]')
                    time.sleep(1)
                    for j in range(countz):
                        msg_boxz.send_keys(msgz)
                        try:
                            driver.find_element_by_xpath('//button[@class="_2lkdt"]').click()
                        except:
                            driver.find_element_by_xpath('//span[@data-icon="send"]').click()
            
    except:
        print("Sorry nothing was found by that name.\n")
        
    choice=input("Do you want to continue?\n1-> YES\tAnything else-> NO\n")
    if '1' in choice:
        pass
    else:
        break

x=input("Don't do anything that harms the experience of other users.\nUse at your own risk\nPress Enter to exit...")
