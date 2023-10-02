from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)  # Users wait between 1 and 2 seconds between tasks
    
    @task
    def post_event(self):
        self.client.post("/events", data="Some test data email checkpoint", headers={"Content-Type": "text/plain"})
        
    @task
    def get_stats(self):
        self.client.get("/stats?interval=60")  # Replace with the desired interval
