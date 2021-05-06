#%%

from selenium import webdriver
from time import sleep


driver=webdriver.Chrome(executable_path='chromedriver')

driver.get("https://10fastfingers.com/typing-test/french")



sleep(3)


text_box = driver.find_element_by_xpath('//*[@id="inputfield"]')

for i in range(1,316):
    machin = driver.find_element_by_class_name('highlight').text
    for j in range(len(machin)):

        text_box.send_keys(machin[j])
        #sleep(0.001)
    text_box.send_keys(" ")
    
