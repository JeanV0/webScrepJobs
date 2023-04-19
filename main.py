from Tools.ReportJobs import ReportJobs
import os  # Módulo que permite a interação com o Sistema Operacional
import csv

from reports.indeedCsv import IndeedToolCsv



if __name__ == "__main__":
    os.chdir("reports/")  # Muda o diretório Atual

    # ------------------------------------------------------------------------
    # Abre o Arquivo CSV Criado para
    writer = csv.writer(open('vagas_ids.csv', 'w', encoding='utf-8', newline=''))
    header = ['ID', 'TITULO', 'LINK']
    writer.writerow(header)
    
    webScraper = ReportJobs()
    webScraper.getJobs('Python development')
    webScraper.extractInfoToSite("São Paulo - SP")
    jobListInfo = webScraper.getJobs()
    
    indeed = IndeedToolCsv()
    indeed.saveCsv(jobListInfo)
    