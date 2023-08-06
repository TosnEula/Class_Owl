from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select    #For the dropdown menu

#Defining web browser data
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'       #Finds the exe for firefox
#options.add_argument("--headless")                 #Runs the driver in the background
s = Service('C:\webDriver\geckodriver.exe')                  #Find webdriver

#Setting up driver and starting website
driver = webdriver.Firefox(service=s, options=options)
driver.get("https://usfonline.admin.usf.edu/pls/prod/bwckschd.p_disp_dyn_sched")

#Find the txt field and enter data
searchBar = Select(driver.find_element(By.NAME, "p_term"))   #Finds the tag for the dropdown menu bar
searchBar.select_by_visible_text("Fall 2023")    #Selects Fall 2023 in the dropdown menu


#Submits the selected term
submitButton = driver.find_element(By.TAG_NAME, "form")
submitButton.submit()


#Waits for the redirect to finish
wait = WebDriverWait(driver, 10)
wait.until(EC.title_is('Class Schedule Search'))

#Finds the coursed ID and scrolls it into view and selects it
courSubjId = driver.find_element(By.CSS_SELECTOR, "[value='COP']")
driver.execute_script("arguments[0].scrollIntoView();", courSubjId)
courSubjId.click()

#Inputs the course Number
courNumInput = driver.find_element(By.ID, "crse_id")
courNumInput.clear()
courNumInput.send_keys("2510")

#Inputs the title of the course
courTitleInput = driver.find_element(By.ID, "title_id")
courTitleInput.clear()
courTitleInput.send_keys("Programming Concepts")


#Unchecks box for showing OPEN ONLY classes
boxUncheck = driver.find_element(By.CSS_SELECTOR, "input[value='Y']") #Uses the CSS Selector method to untick the box
boxUncheck.click()

#Clicks the submit button
#need to find a better way
classSearch = driver.find_element(By.CSS_SELECTOR, "input[value='Class Search']") #Added a way to sesrch by CSS Selector
classSearch.click()


#RESULTS PAGE OF ALL CLASSES
#Waits for the redirect to finish
wait2 = WebDriverWait(driver, 10)
wait2.until(EC.title_is('Class Schedule Listing'))


#Stores the rows of the table as a list
resultsDriver = driver.find_elements(By.XPATH, "//*[@summary= 'This layout table is used to present the sections found']/tbody/tr")


#Deletes the first two rows from the list (Computer Programming and Status rows)
del(resultsDriver[0:2])


#Parses through each sublist within the list of rows 
for a in resultsDriver:
    tdResults = a.find_elements(By.TAG_NAME, "td")

    for x in tdResults:
        print(x.text)


print("-------------------------------------------------------------------------------------------------------------------------------------")
