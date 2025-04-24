from ngrams.tokenizer import tokenizer
from ngrams.ngrams import gen_ngrams, gen_ngram_probs
from ngrams.utils.count import get_counts
def run_app():
	corpus = '''Morality is our understanding of right and wrong that leads us to act with kindness, honesty and fairness. While different cultures have varying moral codes, most share basic values like respecting life and seeking justice. These common principles help societies function peacefully. Some believe morality comes from religion while others see it as a product of human reason and empathy. Difficult choices between competing values show how complex morality can be. However, fundamental ideals like compassion and responsibility create shared ethical ground. True morality involves more than following rules - it requires thoughtful decisions that promote human dignity and wellbeing for all.'''
	n = 2

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

	# generate ngrams
	ngrams = gen_ngrams(vocab=vocab, n = n, ngram = [])
	history_grams = gen_ngrams(vocab = vocab, n = n-1, ngram=[])

	'''
	print("\n")
	print(f"{n}-Grams")
	for ngram in ngrams:
		print(ngram)
	'''
	
	
	counts = get_counts(ngrams, history_grams, tokens)
	probs = gen_ngram_probs(ngrams, counts)

	print('\n')
	print(f"{n}-Gram Probabilities")
	print(probs)
	
	
	
if __name__ == "__main__":
    run_app()
