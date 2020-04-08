import random_name
from locust import HttpLocust, TaskSet, wait_time, between


def login(l):
    l.client.post("/login", {"username": random_name.generate_name(), "passwd": ""})


def logout(l):
    l.client.get("/logout")


def productpage(l):
    l.client.get("/productpage")


class UserBehavior(TaskSet):
    tasks = {productpage: 1}

    # def on_start(self):
    #     login(self)

    # def on_stop(self):
    #     logout(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5000, 9000)
