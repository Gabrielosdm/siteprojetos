logins = {'gym': '123', 'game': '456', 'draw': '1234'}

disciplinas = {'gym': [['Giant ','5/9/2023', 'Shevi2k' ]],
               'game': [['Apex ','15/2/2020', 'Vinicius']],
               'draw': [['Hentai','24/03/2019','Rivetti']]}

detalhes = {'Giant': [['Giant ','5/5/2018 ','5/9/2023']],
            'Apex':[['Apex ','14/03/2019 ','15/2/2020']]}




def validar_login(login, senha):
    return (login in logins) and (logins[login] == senha)

def get_disciplinas(login):
    return disciplinas[login]

def get_detalhes(disciplina):
    return detalhes[disciplina]

def get_detativ(deta):
    return detativ(deta)