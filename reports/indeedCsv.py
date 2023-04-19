import csv


class IndeedToolCsv(object):
    def __init__(self):
        self.title_options = ["Financeiro", "financeiro", "Administrativo", "administrativo"]
        self.exclusor = ["Superior", "superior", "cursando", "Cursando", "formado",
                    "Formado", "Estágio", "Estagiário", "Bilíngue", "estágio",
                    "estagiário", "PCD"]
        
    def checkTitle(self,vaga):
        if any(titulo in vaga for titulo in self.title_options):
            result = True
        else:
            result = False
        return result
    
    def check_superior(self,vaga):
        if any(titulo in vaga for titulo in self.exclusor):
            result = True
        else:
            result = False
        return result
    
    def saveCsv(self,jobListInfo):
        for info in jobListInfo:
            if len(info.button) > 0:
                if self.checkTitle(self, info):
                    if self.check_superior(self, info):
                        pass
                    else:
                        titulo = info.title
                        link = info.job
                        id_v = info.idJob

                        writer = csv.writer(open('vagas_ids.csv', 'a', encoding='utf-8', newline=''))
                        writer.writerow([id_v, titulo, link])
                else:
                    pass