from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(100000000000, 100000000000)

    @task(2)
    def request_all_country_info(Self):
        Self.client.get("/country/egypt")

    @task(1)
    def request_one_country_info(Self):
        Self.client.get("/country/egypt?info=population")

    @task(1)
    def request_some_country_info(Self):
        Self.client.get("/country/egypt?info=name,population")



