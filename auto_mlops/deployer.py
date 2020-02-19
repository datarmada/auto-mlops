import pickle
import tempfile
import requests 

class Deployer():

    def deploy(self, model):
        with tempfile.TemporaryFile() as fp:
            pickle.dump(model, fp)
            res = requests.post("https://cloud.datarmada.com/upload", {"model":fp})
        print(res)