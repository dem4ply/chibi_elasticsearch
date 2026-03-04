import unittest
from chibi_elasticsearch.snippet import build_index_name, list_indices


class Test_build_index_name( unittest.TestCase ):
    def test_should_work( self ):
        result = build_index_name( "some_index" )
        self.assertEqual( 'some_index', result )

    def test_should_work_with_app_name_should_concatenate( self ):
        result = build_index_name( "some_index", app_name="something" )
        self.assertEqual( 'something__some_index', result )


class Test_list_indices( unittest.TestCase ):
    def test_should_work( self ):
        result = list_indices()
        self.assertTrue( result )

    def test_should_return_a_list_of_dicts( self ):
        result = list_indices()
        self.assertIsInstance( result, list )
        for r in result:
            self.assertIsInstance( r, dict )
