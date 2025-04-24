from ngrams.tokenizer import tokenizer
from ngrams.probabilities import gen_ngram_probs

def run_app():
	corpus = '''Text normalization is an essential step in natural language processing that prepares raw text for analysis by converting it into a uniform format. This process helps reduce complexity and improve consistency across different texts. The main goal is to handle variations in how words appear while preserving their core meaning. One common normalization technique involves converting all text to lowercase. This prevents the same word from being treated differently just because of capital letters. For example, "Book" and "book" would become identical after lowercasing. While this simplifies processing, it can sometimes remove meaningful distinctions, such as proper nouns versus common nouns. Punctuation handling is another important aspect. Depending on the application, punctuation marks might be removed entirely, kept as separate tokens, or expanded into words. Contractions like "can't" might be converted to "cannot" for consistency. Similarly, special characters and symbols often get filtered out or replaced with standardized forms. Breaking text into individual words, known as tokenization, presents its own challenges. Some words contain internal punctuation like hyphens or apostrophes that need careful handling. Languages without clear word boundaries, such as Chinese, require specialized tokenization approaches. The choice of tokenization method can significantly impact later processing steps. Many systems remove very common words, often called stop words, which appear frequently but carry little meaning. Words like "the" or "and" might be filtered out to focus on more meaningful terms. However, this isn't always beneficial—some applications, like question answering, may need these words to understand sentence structure. Reducing words to their base forms helps group related terms together. Stemming does this by cutting off word endings, while lemmatization uses vocabulary knowledge to find dictionary forms. For example, both "running" and "ran" might be reduced to "run." These techniques help recognize that different forms of a word share the same core meaning.'''
	n = 3

	# tokenization
	tokens = tokenizer(corpus=corpus, n=n)
	print(f"Tokens: |N| = {len(tokens)}")
	print(tokens)

	# unique words make up vocabulary
	vocab = []
	seen = set()
	for token in tokens:
		if token not in seen:
			vocab.append(token)
			seen.add(token)
	
	print("\n")
	print(f"Vocab: |V| = {len(vocab)}")
	print(vocab)

	# generate ngram probabilities
	probabilities = gen_ngram_probs(vocab=vocab, tokens=tokens, n = n)

	print("\n")
	print(f"{n}-Gram Probabilities")
	print(probabilities)
	
if __name__ == "__main__":
    run_app()
