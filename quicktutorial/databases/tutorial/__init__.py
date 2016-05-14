from sqlalchemy import engine_from_config
from .security import groupfinder
from .models import DBSession, Base,User
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
my_session_factory = SignedCookieSessionFactory('itsaseekreet')
def main(global_config, **settings):
    config = Configurator(settings=settings,
                          root_factory='tutorial.models.RootFactory')
    config.set_session_factory(my_session_factory)
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
    config.add_route('st','/st')
    config.add_route('new_payam','/npayam')
    config.add_route('ersal_payam','/epayam')
    config.add_route('recive_payam','/rpayam')
    config.add_route('new_nameh','/n')
    config.add_route('jquery','/url')
    config.add_route('ersal_nameh','/ersali')
    config.add_route('edit_nameh','/{id}/edit')
    config.add_route('view_nameh','/view/{id}')
    config.add_route('view_namehu','/viewu/{id}')
    config.add_route('kartabl','/nameh')
    config.add_route('pishnevis','/pishnevis')
    config.add_route('eghdam','/eghdam')
    config.add_route('search','/search')
    config.add_route('save','/save')
    config.add_route('imguser','/user/{username}')
    config.add_static_view('deform_static','deform:static/')
    config.add_static_view(name='css',path='tutorial:css')
    config.add_static_view(name='js',path='tutorial:js')
    config.add_static_view(name='img',path='tutorial:images')
    config.add_static_view(name='template',path='tutorial:template')
    config.scan('.views')
    return config.make_wsgi_app()