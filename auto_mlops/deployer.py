import pickle

import requests

class Deployer():
    def __init__(self):
        self.route = None

    def deploy(self, model):
        with open("model,") as fp:
            data = pickle.dump(model, fp)
            res = requests.post("https://cloud.datarmada.com/upload", files={"model": data})
        self.route = res.json()["route"]
        print(f"Your model has been deployed to {self.route}")
        return self.route