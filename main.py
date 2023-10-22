from modules import tools

link = 'https://www.instagram.com/cecaneuft/'

perfil = tools.FindElement.getPerfilInfo(link)

for index,key in enumerate(perfil):
    print(f'{key}:{perfil[key]}\n') 