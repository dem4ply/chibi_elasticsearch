import datetime
import logging

from elasticsearch_dsl import Document, field


logger = logging.getLogger( 'chibi_django.models' )


class Chibi_model( Document ):
    """
    clase basica para usar elastisearch

    Arguments
    ---------
    create_at: datetime.datetime
        fecha en la que se agrebo el modelo
    update_at: datetime.datetime
        fecha en la que se actualizo el modelo
    """
    create_at = field.Date()
    update_at = field.Date()

    def save( self, *args, **kw ):
        if not getattr( self.meta, 'id', False ):
            if getattr( self, 'id', False ):
                self.meta.id = self.id
                del self.id
            if not getattr( self, 'create_at' ):
                self.create_at = datetime.datetime.now( datetime.UTC )
        self.update_at = datetime.datetime.now( datetime.UTC )
        return super().save( *args, **kw )
