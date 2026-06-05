""""Another task under the text classification umbrella is Question Natural Language Inference, or QNLI. This checks if a premise contains enough information to answer a posed question, determining whether the answer can be found in the given text.

Performing different tasks with the `text-classification` pipeline can be done by choosing different models. Each model is trained to predict specific labels and optimized for learning different context within a text.

`pipeline` from the `transformers` library is already loaded for you.

### **Instructions**

- Create a text classification QNLI pipeline using the model `"cross-encoder/qnli-electra-base"` and save as `classifier`.
- Use this classifier to determine if the text provides enough information to answer the question."""


from transformers import pipeline

classifier = pipeline(task= "text-classification", model= "cross-encoder/qnli-electra-base")

results = classifier("Where is the capital of France?, Brittany is known for its stunning coastline.")

print(results)