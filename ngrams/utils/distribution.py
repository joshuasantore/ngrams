from typing import Tuple, Dict
import math
def gen_dist(history: Tuple[str], ngram_probs: Dict[Tuple[str], float]) -> Tuple[(float, Tuple[str])]:
	
	start = 0
	dist = dict()

	# each interval corresponds to the probability of that result (i.e. they go from 0 to 1)
	# need to convert back to normal probability since we're storing in log space
	for ngram in ngram_probs:
		
		# for unigram case
		if len(history) == 0:
			end = start + math.exp(ngram_probs[ngram])
			dist[(start, end)] = ngram
			start = end
		
		# non unigram case
		else:
			# note that we're only including the ngrams that have the appropriate history in our distribution
			if ngram[:len(history)] == history:
				end = start + math.exp(ngram_probs[ngram])
				dist[(start, end)] = ngram
				start = end # make sure we begin our next interval where the last ended
	

	# Need to handle the case that there is no probability distribution(only happens for n > 1) -> return one sentence ending marker (lazy solution)
	if len(list(dist)) == 0:
		dist[(0,1)] = tuple(list(history) + ["</s>"])
		return dist
	
	'''
	If we do have a distribution need to remove the last interval and replace it with an identical interval that ends at *1* to ensure we actually build a probability distribution (probs must add up to 1) : happens for all n
	Steps:
		Save the last interval
		Save the ngram associated with that interval
		delete the last interval
		Save a new interval with the associated ngram that starts at the same value but ends at 1

	'''

	last_interval = list(dist)[-1]
	last_gram = dist[last_interval]
	del dist[last_interval]
	newLastInterval = (last_interval[0], 1) 
	dist[newLastInterval] = last_gram

	return dist

		
