from locust import HttpUser, task, between


class UsuarioWordPress(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.client.get("/", name="[inicio] home")

    @task(5)
    def pagina_inicial(self):
        self.client.get("/", name="Home")

    @task(3)
    def post_individual(self):
        self.client.get("/?p=1", name="Post")

    @task(2)
    def busca(self):
        self.client.get("/?s=hello+world", name="Busca")

    @task(1)
    def wp_login(self):
        self.client.get("/wp-login.php", name="Login")
