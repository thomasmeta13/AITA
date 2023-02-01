from helper import preprocess
import pandas as pd
sample_df = pd.read_csv('aita_sample.csv')
texts = sample_df["post"] # List of "Am I the Asshole" posts
labels = sample_df["label"] # List of moral judgement labels (e.g., 1 for "asshole", 0 for "not an asshole")

# convert labels into binary
# 1 for "Asshole", else 0
labels = [1 if label == "Asshole" else 0 for label in labels]

import openai

# Initialize the OpenAI API client
openai.api_key = "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"

# Extract the contextual embeddings
def response(text):
    return openai.Embedding.create(
          model="text-embedding-ada-002",
          input=text
        )


# Create a dataframe with the embedded texts
# and the labels
df = pd.DataFrame({"text": texts, "label": labels})
df["embedding"] = df["text"].apply(lambda x: response(x)["data"][0]["embedding"])

# save the dataframe to a csv file
df.to_csv("aita_embeddings.csv", index=False, sep="$")
