from time import sleep

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FindElement:
    def getInitalElement(driver, typeElement, element):
        found = False
        tryCount = 50
        while found == False and tryCount > 0:
            try:
                match typeElement:

                    case 'tag':
                        item = driver.find_element(By.TAG_NAME,element)
                        found = True if item else False

                    case 'id':
                        item = driver.find_element(By.ID,element)
                        found = True if item else False
            except:
                # print(tryCount)
                tryCount -= 1
                sleep(0.1)

        return item
    
    def getDriver(link):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(link)

        return driver
    
    def getElements(item, typeElement, element):
        match typeElement:

            case 'tag':
                obj = item.find_elements(By.TAG_NAME,element)

            case 'id':
                obj = item.find_elements(By.ID,element)

            case 'class':
                obj = item.find_elements(by=By.CSS_SELECTOR, value=f'.{element}')
                    
        return obj
    
    def getElement(item, typeElement, element):
        match typeElement:

            case 'tag':
                obj = item.find_element(By.TAG_NAME,element)

            case 'id':
                obj = item.find_element(By.ID,element)

            case 'class':
                obj = item.find_element(by=By.CSS_SELECTOR, value=f'.{element}')
                    
        return obj
    
    def getPerfilInfo(driver):
        perfilDict = dict()

        header = FindElement.getInitalElement(driver,'tag','header')

        divHeader = FindElement.getElement(header,'tag','div')
        divHeader2 = FindElement.getElement(divHeader,'tag','div')
        divSpan = FindElement.getElement(divHeader2,'tag','span')

        imgPerfil = FindElement.getElement(divSpan,'tag','img')

        perfilDict['imgPerfil'] = imgPerfil.get_attribute("src")

        sectionHeader = FindElement.getElement(header,'tag','section')
        sectionDiv = FindElement.getElement(sectionHeader,'class','x6s0dn4')

        perfilDict['perfilTag'] = FindElement.getElement(sectionDiv,'tag','h2').text
        
        sectionUl = FindElement.getElement(sectionHeader,'tag','ul')

        liul = FindElement.getElements(sectionUl,'tag','li')
        
        for li in liul:
            buttonli = FindElement.getElement(li,'tag','button')

            chave = buttonli.text.split()[-1]

            perfilDict[chave] = buttonli.text
            

        sectionDiv2 = FindElement.getElement(sectionHeader,'class','x7a106z')
        divPerfilName = FindElement.getElement(sectionDiv2,'class','x9f619')
        spanDivPerfilName = FindElement.getElement(divPerfilName,'tag','span')

        perfilDict['perfilName'] = spanDivPerfilName.text
        
        descriptionPerfilh1 = FindElement.getElement(sectionDiv2,'tag','h1')

        perfilDict['perfilDescription'] = descriptionPerfilh1.text.replace('\n','<br>')

        divUrl = FindElement.getElement(sectionDiv2,'class', 'x3nfvp2')
        aDivUrl = FindElement.getElement(divUrl, 'tag','a')
        perfilDict['perfilSite'] = f'https://{aDivUrl.text}'
        
        return perfilDict
    
    def getPublis(driver):
        listPubli = list()

        articlePublis = FindElement.getInitalElement(driver,'tag','article')
        articleDiv = FindElement.getElement(articlePublis,'tag','div')
        articleDiv2 = FindElement.getElement(articleDiv,'tag','div')

        publiRows = FindElement.getElements(articleDiv2,'tag','div')

        for publis in publiRows:
            listPublis = FindElement.getElements(articleDiv2,'tag','div')

            for item in listPublis:
                publi = FindElement.getElement(item,'tag','div')

                divA = FindElement.getElement(publi,'tag','a')

                divEmA = FindElement.getElement(divA,'tag','div')

                divEmA2 = FindElement.getElement(divEmA,'tag','div')

                img = FindElement.getElement(divEmA2,'tag','img')

                imgAlt = img.get_attribute("alt")

                imgUrl = img.get_attribute("src")

                print(imgUrl)