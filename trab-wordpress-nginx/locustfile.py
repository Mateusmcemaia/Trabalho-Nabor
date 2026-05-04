from locust import HttpUser, task, between

class UsuarioWordPress(HttpUser):
    wait_time = between(1, 3)

   
    @task
    def post_imagem_media(self):
        self.client.get("/?p=14", name="Cenario 1 - 100kb")
     
     
    @task
    def post_imagem_grande(self):
        self.client.get("/?p=9", name="Cenario 2 - 400kb")

  
    @task
    def post_imagem_maior(self):
        self.client.get("/?p=5", name="Cenario 3 - 900kb")
 
        