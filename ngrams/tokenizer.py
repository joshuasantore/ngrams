from typing import List
import re
def tokenizer(corpus: str, n) -> List[str]:
	
	# Normalization
	corpus = corpus.lower()
	corpus = re.sub(r"[\(\)\"'`~&><:;,\{\}\[\]\|\\_]", "", corpus) # get rid of non sentence terminating punctuation
	corpus = corpus.strip()
	# 

	# sentence segmentation tools for n = 1 case
	sentence_end = " </s>"
	sentence_start = ""

	# adjusting for n != 1 case
	if n != 1:
		sentence_start = "<s> " * (n-1)
		sentence_end = sentence_end * (n-1)
		
	
	corpus = re.sub(r"([^.!?]*.)", sentence_start + r" \1", corpus)
	corpus = re.sub(r"[.?!]", sentence_end + " ", corpus)
	corpus = re.sub(r"  +", " ", corpus)
	
	corpus = corpus.strip()
	
	tokens = corpus.split(" ")
	return tokens
