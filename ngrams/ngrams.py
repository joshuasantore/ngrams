from typing import List, Tuple, Dict
from ngrams.utils.count import get_count	

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
