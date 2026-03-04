from elasticsearch_dsl.connections import connections


def build_index_name( name, app_name=None, ):
    """
    crea el nombre del indice para producion o para pruebas

    Parameters
    ----------
    name: str
    app_name: str
        por default toma el nombre del projecto
    """
    if app_name:
        result = f"{app_name}__{name}"
    else:
        result = name

    is_test = False
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
