import logging
import pickle

import requests
from sklearn.base import BaseEstimator


class Deployer():
    def __init__(self):
        self.route = None

    def deploy(self, model: BaseEstimator):
        if not issubclass(model.__class__, BaseEstimator):
            raise TypeError("Your model must be a scikit-learn model")
        with open("model") as fp:
            data = pickle.dump(model, fp)
            res = requests.post("https://cloud.datarmada.com/upload", files={"model": data})
        if res.status_code == 200:
            self.route = res.json()["route"]
            print(f"Your model has been deployed to {self.route}")
            return self.route
        else:
            logging.error(f"The request responded with the status code {res.status_code}")
            logging.error(res.json())
