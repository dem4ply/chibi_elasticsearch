===================
chibi_elasticsearch
===================


.. image:: https://img.shields.io/pypi/v/chibi_elasticsearch.svg
        :target: https://pypi.python.org/pypi/chibi_elasticsearch

.. image:: https://readthedocs.org/projects/chibi-elasticsearch/badge/?version=latest
        :target: https://chibi-elasticsearch.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


chibi_elasticsearch is a lightweight Python package that provides templates
and reusable snippets for working with Elasticsearch.
It is intended to simplify common tasks such as creating models class.

The package is designed to work with elasticsearch_dsl.


* Free software: WTFPL
* Documentation: https://chibi-elasticsearch.readthedocs.io.


*********
basic use
*********

.. code-block:: python

	from chibi_elasticsearch.models import Chibi_model
	from chibi_elasticsearch.analyzers import name_space, name
	from elasticsearch_dsl import field


	class Person( Chibi_model ):
		name = field.Text(
			analyzer=name, multi=True,
			fields={
				'space': field.Text( analyzer=name_space, multi=True ),
				'keyword': field.Keyword( multi=True ),
			}
		)

	some_one = Person( name="john smith" )
	some_one.save()
	print( "name:", some_one.name )
	print( "create_at:", some_one.create_at )
	print( "update_at:", some_one.update_at )
