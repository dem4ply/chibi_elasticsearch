from elasticsearch_dsl import analyzer, tokenizer


name = analyzer(
    'name',
    tokenizer=tokenizer( 'trigram', 'nGram', min_gram=3, max_gram=4 ),
    filter=[ "lowercase", ],
)

name_space = analyzer(
    'name_space',
    tokenizer='whitespace',
    filter=[ "lowercase", ],
)
