# Week 4 Sentiment Analyzer Analysis Report

My sentiment analyzer had an overall test accuracy of 83% on the regular movie review test set. The challenge set was harder and the overall accuracy dropped to 72%.

The accuracy by category was:
- Negation: 100%
- Sarcasm: 100%
- Mixed sentiment: 60%
- Intensity: 20%
- Domain shift: 80%

The category that hurt the model the most was intensity. It only got 20% correct. The model had trouble telling the difference between mild positive wording such as “fine” and stronger positive wording such as “excellent” or “extraordinary.” Because the model uses TF-IDF features, it mostly pays attention to which words are present and how often they appear. It does not really understand the strength of the feeling the same way a person would.

Mixed sentiment was also harder for the model. It only got 60% correct because some reviews contained both positive and negative wording. The model may focus more on certain words instead of understanding which opinion is more important overall.

One way I would improve the model is by using bigrams so it can preserve some word order and combinations of words instead of only individual words. Another option would be to use a sequence model that reads the sentence in order. This would make the model more complex and could require more computing power and training time.

If I was deploying this model for a company, I would be careful about using it by itself to route angry customers to a human. Even though the regular accuracy was 83%, the challenge set showed that it can fail on harder language. Sarcastic reviews could be especially risky because the words may look positive even when the meaning is negative. I would probably use the model as a first step but send uncertain or difficult reviews to a human for review.
