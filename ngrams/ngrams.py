from typing import List, Tuple, Dict
from ngrams.utils.count import get_counts
import math
import concurrent.futures

def gen_ngrams(vocab: list, n:int, ngram:List[str] = []) -> List[Tuple[str]]:
	result = []

	# return our ngram if it is the right length
	if len(ngram) == n:
		return tuple(ngram)
	
	# else loop through tokens again
	else:
		with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
			futures = [executor.submit(gen_ngrams, vocab, n, ngram + [token]) for token in vocab]
			subres = [future.result() for future in concurrent.futures.as_completed(futures)]
			for res in subres:
				if type(res) == tuple:
					result.append(res)
				else:
					for gram in res:
						result.append(gram)
	return result

def gen_ngram_probs(ngrams: List[Tuple[str]], counts: Dict):
	nonzero_grams = dict()
	for ngram in ngrams:
		ngram_count = counts[ngram]
		history_count = counts[ngram[:-1]]

		# make sure we arent saving zeros or dividing by zero
		# using Maximum Likelihood Estimation
		# saving as logarithms to avoid underflow
		if history_count != 0 and ngram_count != 0:
			nonzero_grams.update({ngram: ((ngram_count/history_count))})
	
	# sorting for ease later
	sorted_grams = sorted(nonzero_grams.items(), key=lambda item: item[1], reverse = True)
	return sorted_grams
