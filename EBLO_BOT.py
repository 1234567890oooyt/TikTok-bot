from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from os import system, name
import chromedriver_binary
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import msvcrt, sys


chromedriver_autoinstaller.install()

def id_check():
    global x
    try:
        a =input("\n Type of issue: ")
        if int(a) == 1:
                x =  2
        elif int(a) == 2:
            x =  5
        elif int(a) == 3:
           x =  6
        elif int(a) == 4:
            x =  7
        elif a != 1 or 2 or 3 or 4:
            id_check()
    except:
        x = id_check()
    return x





def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title EBLO BOT')

logo="""\
▓█████  ▄▄▄▄    ██▓     ▒█████      ▄▄▄▄    ▒█████  ▄▄▄█████▓
▓█   ▀ ▓█████▄ ▓██▒    ▒██▒  ██▒   ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▒███   ▒██▒ ▄██▒██░    ▒██░  ██▒   ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒▓█  ▄ ▒██░█▀  ▒██░    ▒██   ██░   ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
░▒████▒░▓█  ▀█▓░██████▒░ ████▓▒░   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░░ ▒░ ░░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░    ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
 ░ ░  ░▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░    ▒░▒   ░   ░ ▒ ▒░     ░    
   ░    ░    ░   ░ ░   ░ ░ ░ ▒      ░    ░ ░ ░ ░ ▒    ░      
   ░  ░ ░          ░  ░    ░ ░      ░          ░ ░           
             ░         by @evgengrciv            ░                   
"""
print(logo)

print("1. View.\n2. Heart.\n3. Followers.\n4. Shares.\n5. Comment.\n6. Ban\n")

auto = int(input("Mode: "))

if auto == 1 or auto == 2 or auto == 3 or auto == 4 :
    vidUrl = input("TikTok video URL: ")
   
    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome( options=chrome_options)
    driver.set_window_size(1024, 650)

    Views = 0
    Hearts = 0
    Followers = 0
    Shares = 0

if auto == 5:
      
    vidUrl = input("TikTok video URL: ")
    nick_name = input("Nikname of comment: ")
    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome( options=chrome_options)
    driver.set_window_size(1024, 650)

    Views = 0
    Hearts = 0
    Followers = 0
    Shares = 0

if auto == 6:
    print(" 1. Violence \n 2. Bullying \n 3. Behavior with elements of enmity \n 4. Terrorism \n ")
    div_id=id_check()
    vidUrl = input(" TikTok ban video URL: ")
    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
    #device = "Iphone "
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #mobile_emulation = { "deviceName": device }
    #chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome( options=chrome_options)
    driver.set_window_size(1024, 650)

    Views = 0
    Hearts = 0
    Followers = 0
    Shares = 0




def beautify(arg):
    return format(arg, ',d').replace(',', '.')

def title1(): # Update the title IF option 1 was picked.
    global Views
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title EBLO BOT V3 ^| Views Sent: {beautify(Views)} ^| Elapsed Time: {time_elapsed}')

def title2(): # Update the title IF option 2 was picked.
    global Hearts
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title EBLO BOT V3 ^| Hearts Sent: {beautify(Hearts)} ^| Elapsed Time: {time_elapsed}')

def title3(): # Update the title IF option 3 was picked.
    global Followers
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title EBLO BOT V3 ^| Followers Sent: {beautify(Followers)} ^| Elapsed Time: {time_elapsed}')

def title4(): # Update the title IF option 1 was picked.
    global Shares
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title EBLO BOT V3 ^|Shares Sent: {beautify(Shares)} ^| Elapsed Time: {time_elapsed}')



def title5(): # Update the title IF option 1 was picked.
   

    while False:
        global com
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title EBLO BOT V3 ^| com Sent: {beautify(com)} ^| Elapsed Time: {time_elapsed}')

    
def loop1():
    global Views
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop1()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        
        driver.refresh()
        Views += 1000
        print("[+] Views sended!")
        
        sleep(300)
        loop1()
        
    except:
        print("[-] An error occured. Retrying..") 
        driver.refresh()
        loop1()

def loop2():
    global Hearts
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop2()
        
    try:
        sleep(2)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/input').send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/div/button').click()
        
        sleep(5)
        driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
        
        sleep(6)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text.split()
        
        Hearts += int(hearts[0])
        print("[+] Hearts sended!")
        
        sleep(5)
        driver.refresh()
        
        sleep(1800)
        loop2()
        
    except:
        print("[-] An error occured. Retrying..") 
        driver.refresh()
        loop2()

def loop3():
    global Followers
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop3()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click()
        sleep(6)
        folls = driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/span').text.split()
        
        Followers += int(folls[0])
        print("[+] Followers sended!")
        driver.refresh()
        
        sleep(1800)
        loop3()
        
    except:
        print("[-] An error occured. Retrying..")
        driver.refresh()
        loop3()


def loop4():
    global Shares
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop4()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid7\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid7\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9s\"]/div[1]/div/form/button").click()
        
        driver.refresh()
        Shares += 1000
        print("[+] Shares sended!")
        
        sleep(300)
        loop4()
        
    except:
        print("[-] An error occured. Retrying..") 
        driver.refresh()
        loop4()









def loop5():
    
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop5()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid3\"]/div/form/div/input").send_keys(vidUrl)

        
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid3\"]/div/form/div/div").click()

        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div").click()
# тут вставляється посилання на  кнопку з коментом
        sleep(2)
       # driver.findElement(By.DIV_TEXT, "@dark_reno0").click() 
       # res = driver.find_elements_by_xpath("//*[contains(text(), '@dark_reno')]")
        
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), \"@{}\")]//parent::span//following-sibling::button".format(nick_name)))).click()
        sleep(5) 
        driver.refresh()
        print("[+] LIKES sended!")
        
        sleep(300)
        loop5()
        
    except:
        print("[-] An error occured. Retrying..")
        driver.refresh()
        loop5()

def loop6():



    sleep(4)
    
    try:
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[3]/button[4]")
        action.move_to_element(element)
        action.perform()
        sleep(1)
    except:
        print("EROR") #Cant moowe cursor into ... element
        driver.refresh()
        loop6()


        
    try:
        element_2 = driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div").click()
        sleep(1)
    except:
        print("No isue buttoon find")
        driver.refresh()
        loop6()




    try:
        sleep(1)
        element_3 = driver.find_element_by_xpath("/html/body/div[8]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/label[{}]".format(div_id)).click()
    except:
        print("No isue type buttoon find")
        driver.refresh()
        loop6()        

        

    try:
        sleep(2)
        element_4 = driver.find_element_by_xpath("/html/body/div[8]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/div[3]/button").click()
        sleep(1)
        print("Isue sended !")
        driver.refresh()
        loop6()
    except:


        try:
            sleep(2)
            possible_element_4 = driver.find_element_by_xpath("/html/body/div[8]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/label[1]/div").click()
            sleep(1)
            
            try:
                sleep(2)
                element_4 = driver.find_element_by_xpath("/html/body/div[8]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/div[3]/button").click()
                sleep(1)
                print("Isue sended !")
                driver.refresh()
                loop6()
            except:
                print("Isue NOT sended")
                driver.refresh()
                loop6()


        except:
            print("Isue Type not find")
            driver.refresh()
            loop6()




        print("Isue NOT sended")
        driver.refresh()
        loop6()





    # try:
    #     sleep(2)
    #   #  element_5 = driver.find_element_by_xpath("//*[@id=\"tux-modal-7ksyet3q545\"]/div/div/button").click()
    #     element_5 = driver.find_element(By.CLASS_NAME, "tiktok-1l5yils-ButtonFinish ezqf9p619")
    #     sleep(1)
    #     driver.refresh()
    #     loop6()
    # except:
    #     print("No OK find")
    #     driver.refresh()
    #     loop6()



clear()

print(logo)
print("Log:")

if auto == 1:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title1)
    b = threading.Thread(target=loop1)
    
    a.start()
    b.start()
    
elif auto == 2:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title2)
    b = threading.Thread(target=loop2)
    
    a.start()
    b.start()
    
elif auto == 3:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title3)
    b = threading.Thread(target=loop3)
    
    a.start()
    b.start()


elif auto == 4:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title4)
    b = threading.Thread(target=loop4)
    
    a.start()
    b.start()



elif auto == 5:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title5)
    b = threading.Thread(target=loop5)
    
    a.start()
    b.start()

elif auto == 6:
    driver.get(vidUrl)
    
    a = threading.Thread(target=title5)
    b = threading.Thread(target=loop6)
    
    a.start()
    b.start()
    
elif auto == 7:
    print("[+] This program was created by @evgengrciv \n Instagram: https://www.instagram.com/evgengrciv/.")
    input()


else:
    print(f"{auto} is not a valid option. Please pick 1, 2, 3, 4 or 5")
