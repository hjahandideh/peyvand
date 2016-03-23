from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from .models import DBSession, Base

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings,
                          root_factory='tutorial.models.Root')
    config.include('pyramid_chameleon')
    config.add_route('nameh','/nameh')
    config.add_route('nameh_view','/n')
    config.add_route('wiki_view', '/')
    config.add_route('wikipage_add', '/add')
    config.add_route('wikipage_view', '/{uid}')
    config.add_route('wikipage_edit', '/{uid}/edit')




    config.add_route('nameh_page','/nameh/{id}')


    config.add_static_view('deform_static', 'deform:static/')
    config.add_static_view(name='css', path='tutorial:css')
    config.add_static_view(name='js', path='tutorial:js')
    config.add_static_view(name='img', path='tutorial:images')

    config.scan('.views')
    return config.make_wsgi_app()