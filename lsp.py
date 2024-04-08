#lsp, principio de sustitucion de liskov

""" las clases derivadas tienen que ser 
sustituibles por sus clases bases  """ 

""" class Ave:
    def volar(self):
        return "estoy volando"

class Pinguino(Ave):
    def volar(self):
        return "no puedo volar"

def hacer_valor(ave = Ave):
    return ave.volar()

print(hacer_valor(Pinguino()))
 """


class Ave:
    pass
class AveVolador(Ave):
    def volar(self):
        return "estoy volando"

class AveNoVolador(Ave):
    pass