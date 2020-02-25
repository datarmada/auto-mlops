# Deploy your ML models in production painlessly, immediately and scalably

Datarmada aims at **removing all the friction that comes with Machine Learning in production**.
We understand that Data Scientists are not trained to do that, and sometimes they are
not even attracted by this Software Engineering / DevOps aspect.

**This package aims at deploying your scikit-learn model on a server in one line**.

Your model is deployed on an OVH server so that you own your data and it is compliant with European regulations.

## Installation
Install the package python using pip
```
pip install auto-mlops
```

## Deploy your model

Import the package and use the ```Deployer``` class. You can now deploy your already trained scikit-learn model.
**You will be asked for your email address** so that we can keep track of the ownership of the models deployed, and give you
access to monitoring functions in the future.

```python
from auto_mlops import Deployer
from sklearn.linear_model import LogisticRegression

deployer = Deployer()

model = LogisticRegression().fit(X_train, y_train)

deployer.deploy(model)

>> Please enter your email address so that we can keep track of your models:
you@example.com

>> Your model has been deployed to https://cloud.datarmada.com/{id}
```

You can access your route whenever you want through ```deployer.route```
## Make predictions

You can now send data to the route by making a POST request as following
```python
import requests

res = requests.post(
  "https://cloud.datarmada.com/{id}",
  data = {
    "X": your_data
  }
)
print(res.json())
>> { "prediction" : prediction }
```
