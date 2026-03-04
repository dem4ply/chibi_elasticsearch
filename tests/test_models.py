import time
import datetime
import unittest
from unittest.mock import patch
from chibi_elasticsearch.models import Chibi_model


class Test_model( unittest.TestCase ):
    @patch( 'elasticsearch_dsl.Document.save' )
    def test_create_time_should_be_saved_when_call_save( self, save ):
        model = Chibi_model()
        self.assertFalse( model.create_at )
        model.save()
        self.assertTrue( model.create_at )
        self.assertIsInstance( model.create_at, datetime.datetime )
        save.assert_called_once()

    @patch( 'elasticsearch_dsl.Document.save' )
    def test_updated_at_should_be_saved_when_call_save( self, save ):
        model = Chibi_model()
        self.assertFalse( model.update_at )
        model.save()
        self.assertTrue( model.update_at )
        self.assertIsInstance( model.update_at, datetime.datetime )
        save.assert_called_once()

    @patch( 'elasticsearch_dsl.Document.save' )
    def test_created_at_should_not_be_updated_when_call_save( self, save ):
        model = Chibi_model()
        model.save()
        date1 = model.create_at
        model.save()
        date2 = model.create_at
        time.sleep( 0.01 )
        self.assertEqual( date1, date2 )

    @patch( 'elasticsearch_dsl.Document.save' )
    def test_updated_at_should_be_saved_update_when_call_save( self, save ):
        model = Chibi_model()
        model.save()
        date1 = model.update_at
        model.save()
        date2 = model.update_at
        time.sleep( 0.01 )
        self.assertNotEqual( date1, date2 )
