import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import SpaceTokenizer

# recognize based information from document using nlp
def name_recognize(words_list):
    print(f'run name_recognize., args: words_list: {words_list}')
    tokenizer = SpaceTokenizer()
    toks = tokenizer.tokenize(words_list)
    pos = pos_tag(toks)
    chunked_nes = ne_chunk(pos)

    nes = [' '.join(map(lambda x: x[0], ne.leaves())) for ne in chunked_nes if isinstance(ne, nltk.tree.Tree)]
    print(f'finish name_recognize., returns: {nes}')
    return nes