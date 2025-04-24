from typing import List, Tuple, Dict

def get_counts(ngrams: List[Tuple[str]], history_grams: List[Tuple[str]], tokens: List[str]) -> Dict[Tuple[str], float]:
	counts = {}
	for ngram in ngrams:
		counts[ngram] = get_count(ngram, tokens)
	for ngram in history_grams:
		counts[ngram] = get_count(ngram, tokens)
	# 0 length ngram history is number of tokens
	counts[()] = len(tokens)
	return counts


def get_count(ngram: Tuple[str], tokens: List[str]) -> int:
	# in 1 case, need to make sure we don't count words when they appear as subsets
	if len(ngram) == 1:
		return tokens.count(ngram[0])

	else: 
		start = 0
		count = 0
		# looping until cannot form another n gram
		while start + len(ngram) <= (len(tokens) - 1):
			# if the ngram matches our ngram increment the count
			if tuple(tokens[start:start + len(ngram)]) == ngram:
				count+=1
			start+=1
		return count
