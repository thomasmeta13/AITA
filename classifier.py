import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# load the embeddings
df = pd.read_csv("aita_embeddings.csv", sep="$")

# convert X from string to numpy array of floats
X = np.array([np.fromstring(x[1:-1], sep=", ") for x in df["embedding"]])

print("X shape:", X.shape, "Len of first embedding:", len(X[0]))
y = df["label"].tolist()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize the MLP classifier
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000, random_state=0)

# Train the classifier on the training set
mlp.fit(X_train, y_train)


# Print the baseline accuracy
print("Baseline accuracy:", max(y_train.count(0)/len(y_train), y_train.count(1)/len(y_train)))

# Evaluate the classifier on the testing set
accuracy = mlp.score(X_test, y_test)
print("Model accuracy:", accuracy)