# Trained model 
from sklearn import datasets
import pandas as pd
import pickle
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from google.cloud import storage

# import the iris dataset
iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
X.columns = iris.feature_names
y = pd.DataFrame(iris.target)

# split train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# train with Decision Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# predict 
y_pred = clf.predict(X_test)
print("accuracy_score: %.2f" % accuracy_score(y_test, y_pred))

# save the model in a pickle file
pickle.dump(clf, open('./prediction.pickle', 'wb'))

bucket_name = "flower-prediction"
source_file_name = "./prediction.pickle"
destination_blob_name = "prediction.pickle"

storage_client = storage.Client()
bucket = storage_client.create_bucket(bucket_name)
print("Bucket {} created".format(bucket.name))
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)
print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))

