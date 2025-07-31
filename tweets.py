
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# loading tweet dataset
df = pd.read_csv('tweets.csv')  #  it has 'text' and 'target' columns

# drop missing values 
df.dropna(subset=['text', 'target'], inplace=True)

# spliting data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['target'], test_size=0.2, random_state=42)

# vectorize text using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# train logistic regression model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# predict on test set
y_pred = model.predict(X_test_vec)

# print classification report
print(classification_report(y_test, y_pred))

# test on custom tweet
tweet = ["There’s been an explosion downtown!"]
tweet_vec = vectorizer.transform(tweet)
pred = model.predict(tweet_vec)
print("Disaster" if pred[0] == 1 else "Not disaster")
