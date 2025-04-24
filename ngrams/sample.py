from typing import Dict, Tuple, List
from ngrams.utils.distribution import gen_dist
import random

def sample(n: int, ngram_probs: Dict[Tuple[str], float] ) -> str:
	
	sentence = []
	
	# make sure have the proper context
	for i in range(n-1):
		sentence.append("<s>")
		
	# generate words and append to sentence until sentence ending marker is generated
	word = ""
	if n == 1:
		word = next_word((), ngram_probs)
	else:
		word = next_word(tuple(sentence), ngram_probs)
	while word != "</s>":
		sentence.append(word)
		if n == 1:
			word = next_word((), ngram_probs)
		else:
			word = next_word(tuple(sentence[-(n-1):]), ngram_probs)
		
	# return sentence without sentence beginning markers
	return " ".join(sentence[n-1:])

def next_word(history: Tuple[str], ngram_probs: Dict[Tuple[str], float]) -> str:
	# generate a probability distribution for the ngrams associated with the given history
	dist = gen_dist(history, ngram_probs)

	# choose value between 0(inclusive) and 1(exclusive)
	value = random.random()
	for (start, end) in dist:
		if start <= value < end:
			return dist[(start, end)][-1]
