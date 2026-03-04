=======
History
=======

******************
1.2.0 (2026-03-04)
******************

* add shortcut class to do unittest with vcr that ignore all configured hosts
* add function to get all hosts configured

******************
1.1.0 (2026-03-03)
******************

* add logic for build test index using chibi config

	.. code-block:: python

		from chibi.config import configuration
		configuration.elasticsearch.test_app = True
		assert build_index_name( 'hello' ) == 'test__hello'

******************
1.0.0 (2026-03-03)
******************

* definition for base model and analyzers
* configuration handling for connections
* analyzers ready for text processing
* basic model with automatic created_at and updated_at fields

******************
0.0.1 (2026-03-03)
******************

* First release on PyPI.
