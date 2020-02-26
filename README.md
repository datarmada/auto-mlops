# Deploy your ML models in production painlessly, immediately and scalably

Datarmada aims at **removing all the friction that comes with Machine Learning in production**.
We understand that Data Scientists are not trained to do that, and sometimes they are
not even attracted by this Software Engineering / DevOps aspect.

**This package aims at deploying your scikit-learn pipeline on a server in one line**.

Your model is deployed on an OVH server so that you own your data and it is compliant with European regulations.

## Installation
Install the package python using pip
```
pip install auto-mlops
```

## Deploy your model

Import the package and use the ```Deployer``` class.

```python
from auto_mlops import Deployer
deployer = Deployer()
```

You can now deploy your pipeline by passing to the ```deploy``` method a list containing all its elements.
The pipeline elements (except for the last one) must be either :
- A function returning transformed data if your preprocessor doesn't need to be fitted
- An instance of a class implementing ```fit``` and ```transform``` methods otherwise

The last element of the pipeline must be an instance of a class implementing ```fit``` and ```predict``` methods.
```python

from sklearn.linear_model import LogisticRegression

def preprocess(raw_data):
    # preprocess the data
    return preprocessed_data

class Featurizer:
    def fit(self, preprocessed_data, y):
        # fit the featurizer
        return self

    def transform(self, preprocessed_data):
        # transform the data
        return featurized_data

featurizer = Featurizer().fit(preprocessed_data)

log_reg = LogisticRegression()
log_reg.fit(featurized_data, y)

deployer.deploy([preprocess, featurizer, log_reg])

```
Remember your elements must be fitted if they need to !

**You will be asked for your email address** so that we can keep track of the ownership of the models deployed, and give you
access to monitoring functions in the future.

```python
deployer.deploy([preprocess, featurizer, log_reg])

>> Please enter your email address so that we can keep track of your models:
you@example.com

>> Your model has been deployed to https://cloud.datarmada.com/id
```

You can access your route whenever you want through ```deployer.route```
## Make predictions

You can now send data to the route by making a POST request as following
```python
import requests

res = requests.post(
  "https://cloud.datarmada.com/id",
  data = {
    "X": your_raw_data
  }
)

print(res.json())

>> { "prediction" : prediction }
```
