# simple text summarizer using AI

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# only download once
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

class TextSummarizer:
    def __init__(self):
        """Initialize TextSummarizer instance."""
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer()

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower().strip())
        tokens = [self.lemmatizer.lemmatize(t) for t in tokens if t.isalpha() and t not in self.stop_words]
        return " ".join(tokens)

    def extract_keywords(self, text, top_n=5):
        tokens = word_tokenize(text.lower().strip())
        lemmas = [self.lemmatizer.lemmatize(t) for t in tokens if t.isalpha() and t not in self.stop_words]
        freq_dist = nltk.FreqDist(lemmas)
        return [word for word, _ in freq_dist.most_common(top_n)]

    def generate_summary(self, text, num_sentences=3):
        sentences = sent_tokenize(text)
        if len(sentences) <= num_sentences:
            return text

        tfidf_matrix = self.vectorizer.fit_transform(sentences)
        sentence_scores = np.array(tfidf_matrix.sum(axis=1)).ravel()

        # Sort by descending importance
        top_index = sentence_scores.argsort()[::-1][:num_sentences]

        # Keep sentence order as in original text
        summary = " ".join([sentences[i] for i in sorted(top_index)])
        return summary


if __name__ == "__main__":
    text = str(input("Enter text (or press Enter to use sample text): ")).strip()

    if not text:  # fallback
        text = """
        Artificial intelligence is transforming the way we live and work.
        From healthcare to finance, AI systems are making processes more efficient and accurate.
        However, concerns remain about job displacement and ethical use of data.
        Governments and organizations are working to create frameworks for responsible AI development.
        """

    summarizer = TextSummarizer()
    print("\nKeywords:", summarizer.extract_keywords(text))
    print("\nSummary:\n", summarizer.generate_summary(text, num_sentences=2))
