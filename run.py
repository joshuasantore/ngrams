from ngrams.tokenizer import tokenizer
from ngrams.ngrams import gen_ngrams, gen_ngram_probs
from ngrams.utils.count import get_counts
from ngrams.sample import sample

def run_app():
	corpus = '''Mathematical logic is a branch of math that focuses on understanding how reasoning and proof work in a precise and structured way. Unlike everyday logic, which relies on intuition, it uses strict rules to analyze how statements connect, how truth is determined, and how valid conclusions can be drawn from given facts. One key area is propositional logic, which studies simple statements combined with words like and, or, and not, while predicate logic extends this by using variables and quantifiers to express more complex ideas. Another important concept is formal systems, which provide rules for constructing proofs: step-by-step arguments that show whether a statement is true or false. A major discovery in this field is Gödel’s incompleteness theorems, which prove that even the strongest logical systems cannot prove every true statement, revealing fundamental limits in math. Beyond theory, mathematical logic has practical uses in computer science, helping design programming languages, algorithms, and artificial intelligence by ensuring clear and correct reasoning. It also influences philosophy by providing tools to analyze arguments and explore truth. By studying proofs, logical systems, and computability, mathematical logic strengthens our ability to think clearly, avoid errors, and build reliable theories. Its ideas connect abstract math to real-world problems, making it essential not just for mathematicians but also for computer scientists, philosophers, and anyone interested in structured thinking.'''
	n = 1

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

	print('\n')
	print(f'{n}-Gram Sampling')
	for i in range(1):
		sentence = sample(n, probs)
		print(sentence)
		print()
	
if __name__ == "__main__":
    run_app()
