""""Text classification is the process of labeling an input text into a pre-defined category. This can take the form of sentiment - `positive` or `negative` - spam detection - `spam` or `not spam` - and even grammatical errors.

Explore the use of a `text-classification` pipeline for checking an input sentence for grammatical errors.

`pipeline` from the `transformers` library is already loaded for you.

### Instruction

- Create a pipeline for the task `text-classification` and use the model `"abdulmatinomotoso/English_Grammar_Checker"`, saving the pipeline as `grammar_checker`.
- Use the `grammar_checker` to predict the grammatical correctness of the input sentence provided and save as `output`."""

from transformers import pipeline

grammar_check = pipeline(task ="text-classification",model="abdulmatinomotoso/English_Grammar_Checker")

output = grammar_check("I will walk dog")
print(output)