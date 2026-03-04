#!/usr/bin/env python3
import logging
from chibi.config import configuration
from elasticsearch_dsl.connections import connections


logger = logging.getLogger( 'chibi_elasticsearch.config' )


def load_elasticsearch_config():
    connections.configure( **configuration.elasticsearch.connections )


def review_elasticsearch_config():
    default = connections.get_connection()
    if not default.transport.hosts:
        logger.error(
            "no se detecto configuracion de elasticsearch, "
            "ejemplo de configuracion\n"
            "from elasticsearch_dsl.connections import connections"
            "connections.configure( 'default': { 'hosts': 'localhost:80' } )"
        )
        return False
    return True


def check_index_exists( model_class ):
    return model_class._index.exists()
