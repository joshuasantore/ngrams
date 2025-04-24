from typing import List, Tuple
def get_count(ngram: Tuple, tokens: List[str]):
	
	if len(ngram) == 0:
		return len(tokens)
	
	start = 0
	count = 0
	
	# looping until cannot form another n gram
	while start + len(ngram) <= (len(tokens) - 1):
		# if the ngram matches our ngram increment the count
		if tuple(tokens[start:start + len(ngram)]) == ngram:
			count+=1
		start+=1
		
	return count
