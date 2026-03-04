import logging


logger = logging.getLogger( 'chibi_elasticsearch.vcr' )
try:
    from vcr_unittest import VCRTestCase
except ImportError:
    logger.error(
        "No se puede importar los vcrs se nesesita instalar las "
        "dependencias 'pip install chibi_elasticsearch[vcr]'" )
    raise
from chibi_elasticsearch.config import get_all_hosts_in_config


class Chibi_elastic_vcr( VCRTestCase ):
    """
    clase atajo para que los vcr ignoren los hosts de elasticsearch
    """
    def _get_vcr_kwargs( self, **kw ):
        kw = super()._get_vcr_kwargs( **kw )
        kw[ 'ignore_hosts' ] = self.get_all_ignore_hosts()
        return kw

    def get_all_ignore_hosts( self ):
        return get_all_hosts_in_config()
