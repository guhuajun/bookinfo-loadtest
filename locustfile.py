from locust import HttpLocust, TaskSet

def login(l):
    l.client.post("/login", {"username":"jason", "password":""})

def logout(l):
    l.client.post("/logout", {"username":"jason", "password":""})

def productpage(l):
    l.client.get("/productpage")

class UserBehavior(TaskSet):
    tasks = {productpage: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000