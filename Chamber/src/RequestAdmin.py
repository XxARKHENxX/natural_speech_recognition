import ctypes

class RequestPrivilege:
    # Variaveis / Atributos

    # Métodos
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False