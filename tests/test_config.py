import unittest
from chibi.config import configuration
from chibi_elasticsearch.config import load_elasticsearch_config
from chibi_elasticsearch.config import review_elasticsearch_config
from chibi_elasticsearch.snippet import build_index_name


class Test_config( unittest.TestCase ):
    def test_load_elasticsearch_config_should_work( self ):
        load_elasticsearch_config()

    def test_review_should_be_true_if_have_config( self ):
        review_elasticsearch_config()


class Test_build_index_name( unittest.TestCase ):
    def test_when_setup_is_a_test_should_return_prefix_text( self ):
        configuration.elasticsearch.test_app = True
        result = build_index_name( 'hello' )
        self.assertEqual( result, "test__hello" )

    def test_when_it_not_setup_is_a_test_should_return_prefix_text( self ):
        configuration.elasticsearch.test_app = False
        result = build_index_name( 'hello' )
        self.assertEqual( result, "hello" )
