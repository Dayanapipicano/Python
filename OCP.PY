#ocp, principios de abierto/cerrado
 """las clases o modulos funciones 
 abiertas para la extension pero cerradas para la modificacion"""

 class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError 

class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"enviando mensaje a {self.usuario.email}")


class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviado SMS a {self.usuario.sms}")