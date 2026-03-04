#!/usr/bin/env python3
import logging
from chibi.config import configuration
from chibi.snippet.is_type import is_like_list
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


def _get_all_hosts_in_config():
    keys = connections._kwargs.keys()
    conns = list(
        connections.get_connection( alias=alias ) for alias in keys
    )
    hosts = ( c.transport.hosts for c in conns )
    for host in hosts:
        if is_like_list( host ):
            for h in host:
                if isinstance( h, dict ):
                    yield h[ 'host' ]
                else:
                    yield h
        elif isinstance( host, dict ):
            yield host[ 'host' ]
        else:
            yield host


def get_all_hosts_in_config():
    """
    regresa la lista de todos los hosts
    de elasticsearch_dsl.connections.connections
    """
    return list( _get_all_hosts_in_config() )
