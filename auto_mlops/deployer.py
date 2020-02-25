import logging
import pickle
import requests

from auto_mlops.pipeline_wrapper import pipeline_wrapper
from auto_mlops.utils import check_email


class Deployer():
    def __init__(self):
        self.route = None
        self.email = None

    def login(self):
        email = input("Please enter your email address so that we can keep track of your pipelines: \n")
        while not check_email(email):
            email = input("Please enter a valid email address: \n")
        self.email = email

    def deploy(self, pipeline: list):
        if not self.email:
            self.login()

        pipeline_wrapper = pipeline_wrapper(pipeline)

        file = pickle.dumps(pipeline_wrapper)
        res = requests.post(
            "https://cloud.datarmada.com/upload",
            files = { "pipeline" : file },
            data = { "email" : self.email }
        )

        if res.status_code == 200:
            self.route = res.json()["route"]
            print(f"Your pipeline has been deployed to {self.route}")
            return self.route
        else:
            logging.error(f"The request responded with the status code {res.status_code}")
            logging.error(res.json())
