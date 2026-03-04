import unittest
from chibi_elasticsearch.config import load_elasticsearch_config
from chibi_elasticsearch.config import review_elasticsearch_config


class Test_config( unittest.TestCase ):
    def test_load_elasticsearch_config_should_work( self ):
        load_elasticsearch_config()

    def test_review_should_be_true_if_have_config( self ):
        review_elasticsearch_config()
