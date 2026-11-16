from sentiment_analyzer import predict_sentiment

challenge_reviews = {
    "negation": [
        ("The acting was not good.", "neg"),
        ("I was not impressed by this movie.", "neg"),
        ("This is not a film I would recommend.", "neg"),
        ("The story was not interesting at all.", "neg"),
        ("I did not enjoy watching this movie.", "neg"),
    ]
}
challenge_reviews["sarcasm"] = [
    ("Oh wonderful, another two hours I will never get back.", "neg"),
    ("What a masterpiece. I almost fell asleep three times.", "neg"),
    ("Amazing movie, if your goal is to be completely bored.", "neg"),
    ("Best film ever made, said absolutely no one.", "neg"),
    ("I just loved how nothing interesting happened.", "neg"),
]
challenge_reviews["mixed_sentiment"] = [
    ("The cinematography was beautiful, but the story was terrible.", "neg"),
    ("I liked the acting, but the movie itself was boring.", "neg"),
    ("The story was weak, but the ending was surprisingly good.", "pos"),
    ("The movie looked great, but the characters were annoying.", "neg"),
    ("The plot was confusing, but I still enjoyed the movie overall.", "pos"),
]
challenge_reviews["intensity"] = [
    ("The movie was fine.", "pos"),
    ("The movie was pretty good.", "pos"),
    ("The movie was really good.", "pos"),
    ("The movie was excellent.", "pos"),
    ("The movie was absolutely extraordinary.", "pos"),
]
challenge_reviews["domain_shift"] = [
    ("The restaurant had amazing food and great service.", "pos"),
    ("My meal was cold and the service was terrible.", "neg"),
    ("This phone is fast, easy to use, and worth the money.", "pos"),
    ("The laptop battery is awful and dies too quickly.", "neg"),
    ("The hotel room was clean, quiet, and very comfortable.", "pos"),
]
total_correct = 0
total_reviews = 0

for category, reviews in challenge_reviews.items():
    correct = 0

    print("\nCategory:", category)

    for review, actual_label in reviews:
        predicted_label = predict_sentiment(review)

        print("Review:", review)
        print("Actual:", actual_label)
        print("Predicted:", predicted_label)

        if predicted_label == actual_label:
            correct += 1
            total_correct += 1

        total_reviews += 1
        print()

    category_accuracy = correct / len(reviews)
    print("Accuracy for", category, ":", category_accuracy)

overall_accuracy = total_correct / total_reviews
print("\nOverall challenge accuracy:", overall_accuracy)
