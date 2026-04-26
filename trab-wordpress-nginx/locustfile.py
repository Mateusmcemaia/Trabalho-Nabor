from locust import HttpUser, task, between

class UsuarioWordPress(HttpUser):
    wait_time = between(1, 3)

    @task
    def post_imagem_grande(self):
        self.client.get("/?p=5", name="Cenario 1 - Imagem 1MB")

    @task
    def post_texto(self):
        self.client.get("/?p=12", name="Cenario 2 - Texto 500kb")

    @task
    def post_imagem_media(self):
        self.client.get("/?p=9", name="Cenario 3 - Imagem 300kb")