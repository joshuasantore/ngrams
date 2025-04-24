from ngrams.tokenizer import tokenizer
from ngrams.ngrams import gen_ngrams

def run_app():
	corpus = '''Philosophy is the pursuit of understanding the fundamental nature of existence, knowledge, and value. It seeks to unravel the deepest questions about reality, consciousness, and meaning through reasoned inquiry rather than empirical observation alone. Unlike other disciplines that focus on specific aspects of the world, philosophy examines the underlying principles that shape thought, ethics, and perception. It challenges assumptions, explores the limits of human understanding, and engages with abstract concepts such as truth, justice, and beauty. Philosophers employ logic, critical analysis, and reflection to navigate complex ideas, often arriving at conclusions that provoke further questioning rather than definitive answers. The discipline branches into metaphysics, which considers the nature of being; epistemology, which studies knowledge; ethics, which examines moral principles; and aesthetics, which explores art and beauty. Through dialogue and debate, philosophy fosters intellectual humility, encouraging individuals to recognize the limits of their own perspectives while striving for greater clarity. It is both an ancient tradition and a living practice, continuously evolving as new ideas emerge and old ones are reinterpreted. Philosophy does not provide easy solutions but instead cultivates a deeper appreciation for the complexities of life. By examining the foundations of human thought, it invites us to reflect on how we perceive the world, relate to others, and make meaningful choices. In this way, philosophy remains essential, not as a set of doctrines, but as a method of inquiry that enriches our capacity to think critically and live thoughtfully. Its value lies not in final answers but in the ongoing pursuit of wisdom. Philosophy also serves as a bridge between disciplines, connecting the insights of science, art, religion, and politics into a broader framework of understanding. It asks how we ought to live, not just as individuals but as a society, and questions the structures that govern our lives. By examining concepts like freedom, power, and identity, philosophy reveals the tensions between personal desires and collective responsibilities. It encourages skepticism toward dogma while fostering open-mindedness, allowing ideas to be tested and refined over time. Through its emphasis on dialogue, philosophy nurtures empathy, as engaging with diverse perspectives deepens our comprehension of human experience. Ultimately, it is a tool for self-examination, pushing us to confront our biases and assumptions in the search for truth. Without prescribing rigid conclusions, philosophy offers a space for contemplation, where uncertainty is not a weakness but an invitation to deeper inquiry. Its enduring relevance lies in its ability to adapt, addressing timeless questions while responding to the ever-changing world around us.'''
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

	# generate ngrams
	ngrams = gen_ngrams(vocab=vocab, n = n, ngram = [])

	print("\n")
	print(f"{n}-Grams")
	for ngram in ngrams:
		print(ngram)
	
	
if __name__ == "__main__":
    run_app()
