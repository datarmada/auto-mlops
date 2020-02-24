import logging
import pickle

import requests
from sklearn.base import BaseEstimator
from auto_mlops.utils import check_email


class Deployer():
    def __init__(self):
        self.route = None
        self.email = None

    def login(self):
        email = input("Please enter your email address so that we can keep track of your models.")
        while not check_email(email):
            email = input("Please enter a valid email address")
        self.email = email

    def deploy(self, model: BaseEstimator):
        if not self.email:
            self.login()
        if not issubclass(model.__class__, BaseEstimator):
            raise TypeError("Your model must be a scikit-learn model")

        data = pickle.dumps(model)
        res = requests.post("https://cloud.datarmada.com/upload", files={"model": data})

        if res.status_code == 200:
            self.route = res.json()["route"]
            print(f"Your model has been deployed to {self.route}")
            return self.route
        else:
            logging.error(f"The request responded with the status code {res.status_code}")
            logging.error(res.json())
