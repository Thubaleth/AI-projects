"""Dynamic category assignment enables a model to classify text into predefined categories, even without prior training for those categories.

Using Hugging Face’s `pipeline()` for the `zero-shot-classification` task, provide the text and predefined categories to identify the best match.

Build a classifier to predict the label for the input `text`, which is a news headline already loaded for you.

The `pipelines` from the `transformers` library is preloaded for your convenience.

**Note:** We are using a customized version of the pipeline to help you learn how to use these functions without needing to download the model.

### **Instructions**

- Build the pipeline and save as `classifier`.
- Create a list of the labels - `"politics"`, `"science"`, `"sports"` - and save as `categories`.
- Predict the label of `text` using the classifier and predefined categories."""

from transformers import pipeline

classifier = pipeline("zero-shot-classification")

# Candidate labels
categories = ["politics","science","sports"]


# Predict the category
result = classifier(categories)


print(result["labels"][0])
