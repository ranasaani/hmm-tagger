######### hmm-tagger.py #########

from Tagger import Tagger # import the tagging controller
import os # for path info


# initialize a tagging object with the cleaned corpus file(s)
t = Tagger(os.getcwd()+'/', ['text_1.txt', 'text_2.txt', 'text_3.txt'], ['text_5.txt'])

# perform ten-fold cross-validation
t.run_test_cycles()
