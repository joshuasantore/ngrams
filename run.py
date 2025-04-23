from ngrams.tokenizer import tokenizer
from ngrams.probabilities import gen_ngram_probs

def run_app():
	corpus = ""
	n = 2
	tokens = tokenizer(corpus=corpus, n=n)
     
	vocab = []
	seen = set()
	for token in tokens:
		if token not in seen:
			vocab.append(token)
			seen.add(token)
	
	probabilities = gen_ngram_probs(vocab=vocab, tokens=tokens, n = n)
	print("Tokens:")
	print(tokens)

	print(f"{n}-Gram Probabilities")
	print(probabilities)
	
if __name__ == "__main__":
    run_app()
