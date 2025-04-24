from typing import List, Tuple, Dict
from ngrams.utils.count import get_count
import math

def gen_ngrams(vocab: list, n:int, ngram:List[str] = []) -> List[Tuple[str]]:
	res = []

	# return our ngram if it is the right length
	if len(ngram) == n:
		return tuple(ngram)
	
	# else loop through tokens again
	else:
		for token in vocab:
			# recursively call function with one more word in our ngram
			subres = gen_ngrams(vocab, n, ngram + [token])

			# if what we get is a tuple we can append it to our res
			if type(subres) == tuple:
				res.append(subres)

			# if not we need to make sure we don't append a list to our result and instead append the contents aka the ngrams inside
			else:
				for gram in subres:
					res.append(gram)
				
	return res

def gen_ngram_probs(ngrams: List[Tuple[str]], tokens: List[str]):
	nonzero_grams = dict()

	for ngram in ngrams:

		ngram_count = get_count(ngram, tokens)
		history_count = get_count(ngram[:-1], tokens)

		# make sure we arent saving zeros or dividing by zero
		# using Maximum Likelihood Estimation
		# saving as logarithms to avoid underflow
		if history_count != 0 and ngram_count != 0:
			nonzero_grams.update({ngram: (math.log(ngram_count/history_count))})
	
	# sorting for ease later
	sorted_grams = sorted(nonzero_grams.items(), key=lambda item: item[1], reverse = True)
	return sorted_grams
