# Deploy your ML pipelines effortlessly, scalably and reliably

Datarmada wants to **remove all the friction that comes with Machine Learning in production**.
We understand that Data Scientists are not trained to do that, and sometimes they are
not even attracted by this Software Engineering / DevOps aspect. With this package, we make a first
step in this direction.

**auto-mlops aims at deploying your machine learning pipeline on a server in one line**.

Your pipeline is deployed on an OVH server.

## Installation
Install the package python using pip
```
pip install auto-mlops
```

## Deploy your pipeline

Import the ```Deployer``` class from the package.

```python
from auto_mlops import Deployer
deployer = Deployer()
```

Now, deploy your pipeline by passing to the ```deploy``` method a list containing all of its elements.
The pipeline elements (except for the last one) must be either :
- A function returning transformed data if your pipeline element doesn't need to be fitted
- An instance of a class implementing a ```transform``` method

The last element of the pipeline must be an instance of a class a with a ```predict``` method, such as a 
scikit-learn model.

```python

from sklearn.linear_model import LogisticRegression

def preprocess(raw_data):
    # preprocess the data
    return preprocessed_data

class Featurizer:
    def transform(self, preprocessed_data):
        # transform the data
        return featurized_data

log_reg = LogisticRegression()
log_reg.fit(featurized_data, y)

deployer.deploy([preprocess, featurizer, log_reg])

```
**Remember your elements must be fitted if they need to !**

**You will be asked for your email address** so that we can keep track of the ownership of the pipelines deployed
and to reach you out if a problem shows up.

<pre>
deployer.deploy([preprocess, featurizer, log_reg])

>> Please enter your email address so that we can keep track of your pipelines:
you@example.com

>> Your pipeline has been deployed to:
<u>https://cloud.datarmada.com/<i>{python-version}</i>/<i>{id}</i></u>
</pre>

You can access your route whenever you want through ```deployer.route```
## Make predictions

You can now send data to the route by making a POST request as following
```python
import requests

res = requests.post(
  "https://cloud.datarmada.com/{python-version}/{id}",
  json = {
    "data": your_raw_data
  }
)

print(res.json())
>> { "prediction" : prediction }
```

It may be possible that one of the package you are using is not available in the environment we are deploying your model. 
If you receive an error saying so, please email us at contact@datarmada.com so that we can fix it.