from chibi.config import configuration
from elasticsearch_dsl.connections import connections


def build_index_name( name, app_name=None, ):
    """
    crea el nombre del indice para producion o para pruebas

    Para asirnar que es una prueba se usa la configuracion de chibi

    Parameters
    ----------
    name: str
    app_name: str
        por default toma el nombre del projecto

    Example
    -------
    >>>from chibi.config import configuration
    >>>configuration.elasticsearch.test_app = True
    >>>assert build_index_name( 'hello' ) == 'test__hello'
    >>>configuration.elasticsearch.test_app = False
    >>>assert build_index_name( 'hello' ) == 'hello'
    """
    if app_name:
        result = f"{app_name}__{name}"
    else:
        result = name

    is_test = bool( configuration.elasticsearch.test_app )
    if is_test:
        return f"test__{result}"
    return result


def list_indices():
    es = connections.get_connection()
    return es.cat.indices( format='json' )


def index_exists( model_class ):
    return model_class._index.exists()


def create_index_if_not_exists( model_class ):
    if not index_exists( model_class ):
        model_class.init()
