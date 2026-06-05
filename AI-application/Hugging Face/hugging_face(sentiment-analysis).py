from transformers import pipeline
#Sentiment analysis 
classifier = pipeline("sentiment-analysis")

results = classifier("I hate huggging face")

print(results)
