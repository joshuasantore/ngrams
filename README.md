# ngrams
Just playing around with using ngram language models to generate sentences

## Setup/Deployment
1. add a small corpus of sentences on line 7 of run.py
2. specify n-gram length(1, 2, 3, etc) on line 8 of run.py (very slow for anything above 3 at 300 words ish)
2. run run.py

## Some Notes
- Runs very slowly for larger n / longer corpora.

  A lot of ways to optimize in the future, not limited to threading and replacing certain data structures with faster alternatives.
  When I built this I was more focused on the logic and making everything work than I was with making it work as quickly as possible.

- No way to save models.

  I don't think it would be very hard to implement this. It's really just as simple as dumping the probabilities and ngrams to a csv or maybe an sqlite3 database.

- My implementation is based on what I learned studying Speech and Language Processing 3rd Edition (draft) by Jurafsky and Martin online.

  I tried to use most of what they explained, although I left out any type of smoothing because I wanted to move on to other things. If I were to implement I would probably want to add an optional parameter to specify between No Smoothing, Laplace Smoothing, Interpolation, and Backoff.

- My tokenizer is awful.

  It won't work on any text that isn't given as one big string of sentences. Even then, it still sometimes does not work. This would be the first thing I fix in the future, preferably so that I could provide a text file (or list of files) as a corpus. I think that would be much more convenient in the grand scheme of things. It gets the job done for my test cases at least. Also, because I'm working with ngrams, I opted out of using Byte Pair Encoding, since I do want my tokens to be words. I would love to experiment with a model that does use BPE though.
