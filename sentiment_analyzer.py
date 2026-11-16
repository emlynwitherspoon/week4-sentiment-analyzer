import nltk
from nltk.corpus import movie_reviews
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

nltk.download("movie_reviews")

reviews = []
labels = []

for fileid in movie_reviews.fileids():
    reviews.append(movie_reviews.raw(fileid))
    labels.append(movie_reviews.categories(fileid)[0])

X_train, X_test, y_train, y_test = train_test_split(
    reviews,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)

print("Training reviews:", len(X_train))
print("Testing reviews:", len(X_test))
print("Positive reviews:", labels.count("pos"))
print("Negative reviews:", labels.count("neg"))
vectorizer = TfidfVectorizer(max_features=5000)

X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vectors, y_train)

y_pred = model.predict(X_test_vectors)

accuracy = accuracy_score(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(matrix)

print(
    "The model sees each review as word features and how often they appear, "
    "not the exact order the words appeared in."
)
def predict_sentiment(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    return prediction

if __name__ == "__main__":
    sample_review = "The movie was entertaining and I really enjoyed it."
    print("Sample prediction:", predict_sentiment(sample_review))
