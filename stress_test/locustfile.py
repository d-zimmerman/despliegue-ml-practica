import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(5, 15)

    @task(1)
    def index(self):
        self.client.get('/')

    @task(3)
    def predict(self):
        self.client.post('/predict', params={'text': 'dolar'})

    def on_start(self):
        pass
