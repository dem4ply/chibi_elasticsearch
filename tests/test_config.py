import unittest
from chibi.config import configuration
from chibi_elasticsearch.config import load_elasticsearch_config
from chibi_elasticsearch.config import review_elasticsearch_config
from chibi_elasticsearch.config import get_all_hosts_in_config
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


class Test_get_all_hosts( unittest.TestCase ):
    def test_should_return_all_hosts( self ):
        hosts = get_all_hosts_in_config()
        self.assertTrue( hosts )

    def test_all_hosts_should_be_strings( self ):
        hosts = get_all_hosts_in_config()
        self.assertTrue( hosts )
        for host in hosts:
            self.assertIsInstance( host, str )

    def test_other_config_should_work( self ):
        from elasticsearch_dsl import connections

        connections.configure(
            default={'hosts': 'localhost'},
            dev={
                'hosts': ['esdev1.example.com:9200'],
            }
        )

        hosts = get_all_hosts_in_config()
        self.assertEqual( hosts, [ 'localhost', 'esdev1.example.com' ] )
