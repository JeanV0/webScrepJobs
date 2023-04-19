from datetime import date  # Importando o Módulo para trabalhar com Datas
from time import sleep  # Permite adicionar tempos de espera no código
from selenium import webdriver  # Implementações Web do Selenium
from selenium.webdriver.common.keys import Keys # Envio de Inputs para Web

class ReportJobs(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.__drive = webdriver.Chrome("C:\\Users\\geova\\anaconda3\\self.chrome__drive.exe", options=options)
        
    def getJobs(keyWord, self):
        self.__drive.get('https://br.indeed.com/') 
        jobInput = self.__drive.find_element_by_name('q') 
        jobInput.clear() 
        jobInput.send_keys(keyWord)
        jobInput.send_keys(Keys.RETURN)
        
    def extractInfoToSite(self, region):
        self.__drive.find_element_by_xpath('//a[text()="Busca Avançada de Vagas"]').click()

        self.__drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.__drive.find_element_by_xpath('//input[@id="norecruiters"]').click()

        local = self.__drive.find_element_by_xpath('//input[@id="where"]')
        local.clear()
        
        # local.send_keys('São Paulo, SP')

        local.send_keys(region)

        self.__drive.find_element_by_xpath('//select[@id="fromage"]//option[@value="3"]').click()

        self.__drive.find_element_by_xpath('//select[@id="limit"]//option[@value="50"]').click()
        self.__drive.find_element_by_xpath('//select[@id="sort"]//option[@value="date"]').click()

        sleep(2)
        try:
            self.__drive.find_element_by_xpath('//button[@id="onetrust-accept-btn-handler"]').click()
        except:
            raise ValueError('Could not find')
        
        jobList = (self.__drive.find_elements_by_xpath('//div[@id="mosaic-provider-jobcards"]/a'))
        idsList = [vaga.get_attribute('id') for vaga in jobList]
        self.idsList = list(set(idsList))
        self.jobList = [vaga.get_attribute('href') for vaga in jobList]
        
    def getJobs(self):
        jobListInfo = []
        for job in self.jobList:
            self.__drive.get(job)  
            button = self.__drivefind_elements_by_xpath('//button[@id="indeedApplyButton"]')
            title = self.__drivefind_element_by_css_selector('h1').text
            idJob = self.idsList[self.jobList.index(job)]
            if idJob is None:
                pass
            else:
                jobListInfo.append({button, title, idJob})
        
        return jobListInfo