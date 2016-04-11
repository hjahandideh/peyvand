from sqlalchemy import engine_from_config
from tutorial.security import groupfinder
from .models import DBSession, Base,User
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
def main(global_config, **settings):
    config = Configurator(settings=settings,
                          root_factory='tutorial.models.RootFactory')
    config.include('pyramid_chameleon')
    authn_policy = AuthTktAuthenticationPolicy(
        settings['tutorial.secret'],callback=groupfinder,
        hashalg='sha512')

    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config.add_route('login','/')
    config.add_route('view','/username')
    config.add_route('logout','/logout')
    config.add_route('user','/user')
    config.add_route('nameh','/nameh')
    config.add_route('nameh_view','/n')
    config.add_route('nameh_page','/nameh/{id}')
    config.add_static_view('deform_static','deform:static/')
    config.add_static_view(name='css',path='tutorial:css')
    config.add_static_view(name='js',path='tutorial:js')
    config.add_static_view(name='img',path='tutorial:images')
    config.scan('.views')
    return config.make_wsgi_app()