from modules import tools

link = 'https://www.instagram.com/cecaneuft/'

driver = tools.FindElement.getDriver(link)
# x9f619
perfil = tools.FindElement.getPerfilInfo(driver)

publis = tools.FindElement.getPublis(driver)

# for index,key in enumerate(perfil):
#     print(f'{key}:{perfil[key]}\n') 

# print(publis);