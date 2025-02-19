from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
date_range = 0
import time
import datetime
PATH = "C:\Webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://dineoncampus.com/FLPoly/whats-on-the-menu")
lunchItemList = []
lunchDescList = []
lunchPortionList = []
lunchCalorieList = []
lunchLocationList = []
lunchBalVeganList = []
dinnerBalVeganList = []
dinnerItemList = []
dinnerDescList = []
dinnerPortionList = []
dinnerCalorieList = []
dinnerLocationList = []
tableNames = []
tableSums = []
images = []
mealTypes = []
current_date = datetime.datetime(2021,4,8)
outFile = open("WellnessDiningMenu.txt","w") #Open the output file
date_range = int(input("Enter the number of days to be in the file: "))

for i in range(date_range):
    dateLink = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID, "calendarDropdown__BV_toggle_"))#waits till the dinner tab is loaded, meaning waiting till the webpage is fully loaded
            )
    dateLink.click()
    days = driver.find_elements_by_css_selector('span.cell.day')
    for j in range(len(days)):
        if(days[j].text != ""):
            if "0" + days[j].text == current_date.strftime("%d") or days[j].text == current_date.strftime("%d"):
                days[j].click()
                current_date += datetime.timedelta(days=1)
            if current_date.strftime("%d") == "01":
                dateLink.click()
                nextBtn = driver.find_element_by_css_selector('span.next')
                nextBtn.click()
    lunchDescList.clear()
    lunchPortionList.clear()
    lunchCalorieList.clear()
    lunchLocationList.clear()
    lunchBalVeganList.clear()
    lunchItemList.clear()
    dinnerBalVeganList.clear()
    dinnerItemList.clear()
    dinnerDescList.clear()
    dinnerPortionList.clear()
    dinnerCalorieList.clear()
    dinnerLocationList.clear()
    tableNames.clear()
    tableSums.clear()
    images.clear()
    mealTypes.clear()
    previousText = ""
    try:
        time.sleep(2)
        #For Lunch menu
        link = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Dinner"))#waits till the dinner tab is loaded, meaning waiting till the webpage is fully loaded
            )
        allItems = driver.find_elements_by_css_selector('td')#selects all the food items stored in the table that is the menu
        allTables = driver.find_elements_by_css_selector('table')#selects all the tables on the website
        tableNames = driver.find_elements_by_css_selector('caption')#gets the names of all the tables on the website
        time.sleep(2)
        for i in range(0,len(allItems),3):
            images.append(allItems[i].find_elements_by_css_selector('img'))#Looks for all images in table        
          
        for i in range(len(allTables)):
            tableSums.append(len(allTables[i].find_elements_by_css_selector('td'))) #checks the amount of cells in the menu        

        for j in range(len(allTables)):
            for i in range(int((tableSums[j])/3)):
                lunchLocationList.append(tableNames[j].text)#distributes the correct table names to the right amount of cells
        
        for i in range(0,len(allItems),3):
            itemtext = allItems[i].text
            x = itemtext.splitlines()#splits the first item into necessary pieces
            if x[0] != "Chef's Choice" and previousText != x[0]: #makes sure the item name is not a duplicate or a useless name
                lunchItemList.append(x[0])
                if x[2] != "":
                    if x[2] != "Nutritional Info":
                        lunchDescList.append(x[2])#ensures the description exists
                    else:
                        lunchDescList.append("") 
                else:
                    lunchDescList.append("") 
                
                previousText = x[0]
                lunchPortionList.append(allItems[i+1].text)#appends the rest of the items to there respective lists
                lunchCalorieList.append(allItems[i+2].text + " calories")
                if images[int(i/3)] == []:
                    mealString = ""
                    lunchBalVeganList.append(mealString)
                else:
                    mealTypes = images[int(i/3)]
                    mealString = ""
                    for j in range(len(mealTypes)):
                        if mealTypes[j].get_attribute('src') == "https://dineoncampus.com/img/icon_vegetarian_200px.png":
                            mealString = mealString + "Vegetarian!"
                        if mealTypes[j].get_attribute('src') == "https://dineoncampus.com/img/icon_vegan_200px.png":
                            mealString = mealString + "Vegan!"
                        if mealTypes[j].get_attribute('src') == "https://dineoncampus.com/img/icon_balanced_200px.png":
                            mealString = mealString + "Balanced!"
                    lunchBalVeganList.append(mealString)
            else:
                lunchItemList.append("Chef's Choice or Same as previous entry AKA null") #null cases to skip in the file appending
                lunchDescList.append("null")
                lunchPortionList.append("null")
                lunchCalorieList.append("null")
                lunchBalVeganList.append("null")
            
        link.click()
        time.sleep(5) #ensures the dinner page is loaded before grabbing information
        allItems = driver.find_elements_by_css_selector('td')
        tableNames.clear()#clearing of some lists
        tableSums.clear()
        images.clear()
        allTables = driver.find_elements_by_css_selector('table')
        tableNames = driver.find_elements_by_css_selector('caption')
        previousText = ""
        #now the same thing that happened for lunch, happens for dinner
        for i in range(0,len(allItems),3):
            images.append(allItems[i].find_elements_by_css_selector('img'))#Looks for all images in table        
            
        for i in range(len(allTables)):
            tableSums.append(len(allTables[i].find_elements_by_css_selector('td')))        

        for j in range(len(allTables)):
            for i in range(int((tableSums[j])/3)):
                dinnerLocationList.append(tableNames[j].text)
        
        for i in range(0,len(allItems),3):
            itemtext = allItems[i].text
            x = itemtext.splitlines()
            if x[0] != "Chef's Choice" and previousText != x[0]:
                dinnerItemList.append(x[0])
                if x[2] != "":
                    if x[2] != "Nutritional Info":#ensures the description exists
                        dinnerDescList.append(x[2])
                    else:
                        dinnerDescList.append("") 
                else:
                    dinnerDescList.append("") 
                previousText = x[0]
                dinnerPortionList.append(allItems[i+1].text)
                dinnerCalorieList.append(allItems[i+2].text + " calories")
                if images[int(i/3)] == []:
                    mealString = ""
                    dinnerBalVeganList.append(mealString)
                else:
                    mealTypes = images[int(i/3)]
                    mealString = ""
                    for j in range(len(mealTypes)):
                        if mealTypes[j].get_attribute('src') == "https://dineoncampus.com/img/icon_vegetarian_200px.png":
                            mealString = mealString + "Vegetarian!"
                        if mealTypes[j].get_attribute('src') == "https://dineoncampus.com/img/icon_vegan_200px.png":
                            mealString = mealString + "Vegan!"
                        if mealTypes[j].get_attribute('src') == "https://dineoncampus.com/img/icon_balanced_200px.png":
                            mealString = mealString + "Balanced!"
                    dinnerBalVeganList.append(mealString)
            else:
                dinnerItemList.append("null")
                dinnerDescList.append("null")
                dinnerPortionList.append("null")
                dinnerCalorieList.append("null")
                dinnerBalVeganList.append("null")
        
    except:
        outFile.write("There was no food items for: ")
    current_date -= datetime.timedelta(days=1)
    outFile.write("Wellness Dining Menus for "+current_date.strftime("%x")+"\n")#Keeps the date of the web scraping
    current_date += datetime.timedelta(days=1)
    outFile.write("Lunch Menu:\n")#Shows that this is the Lunch menu
    
    for i in range(len(lunchDescList)):
        if lunchCalorieList[i]!= "null":#copies the lists to a file if they are not null
            outFile.write(lunchLocationList[i]+";"+lunchItemList[i]+";"+lunchCalorieList[i]+";"+lunchPortionList[i]+";"+lunchBalVeganList[i]+";"+lunchDescList[i]+";\n")    
    for i in range(len(lunchDescList),len(lunchItemList)):
        if lunchCalorieList[i]!= "null":#copies the lists to a file if they are not null
            outFile.write(lunchLocationList[i]+";"+lunchItemList[i]+";"+lunchPortionList[i]+";"+lunchCalorieList[i]+";"+lunchBalVeganList[i]+";\n")

    outFile.write("Dinner Menu:\n")#Shows that this is the Dinner menu

    for i in range(len(dinnerDescList)):
        if dinnerCalorieList[i]!= "null":#copies the lists to a file if they are not null
            outFile.write(dinnerLocationList[i]+";"+dinnerItemList[i]+";"+dinnerCalorieList[i]+";"+dinnerPortionList[i]+";"+dinnerBalVeganList[i]+";"+dinnerDescList[i]+";\n")
            
    for i in range(len(dinnerDescList),len(dinnerItemList)):
        if dinnerCalorieList[i]!= "null":#copies the lists to a file if they are not null
            outFile.write(dinnerLocationList[i]+";"+dinnerItemList[i]+";"+dinnerPortionList[i]+";"+dinnerCalorieList[i]+";"+dinnerBalVeganList[i]+";\n")

outFile.close()# close the outfile
driver.quit()#quits the file
                

    
