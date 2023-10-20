from modules import tools

driver = tools.FindElement.getDriver()

perfil = tools.FindElement.getPerfilInfo(driver)

print(f'Text: {perfil}')