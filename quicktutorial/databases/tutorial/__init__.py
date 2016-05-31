from .models import Session, Base,User
from pyramid.session import SignedCookieSessionFactory
my_session_factory = SignedCookieSessionFactory('itsaseekreet')
from pyramid.config import Configurator
import sqlalchemy
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .models import Base, Session
from .models import groupfinder, RootFactory


def main(global_config, **settings):
    # Configure our authorization policy
    authentication = AuthTktAuthenticationPolicy(settings['session.secret'],
                                                 callback=groupfinder,hashalg='sha512')
    authorization= ACLAuthorizationPolicy()

    # Create the Pyramid Configurator.
    config = Configurator(settings=settings, root_factory=RootFactory,
                          authentication_policy=authentication,
                          authorization_policy=authorization)

    config.include('pyramid_chameleon')

    # Initialize database
    engine = sqlalchemy.engine_from_config(settings, prefix="sqlalchemy.")
    Session.configure(bind=engine)
    Base.metadata.bind = engine


    config.add_route('login','/')
    config.add_route('view','/username')
    config.add_route('modir','/modirusername')
    config.add_route('new_etla','/new_etla')
    config.add_route('view_etla','/{id}/view_etla')
    config.add_route('logout','/logout')
    config.add_route('user','/user')
    config.add_route('st','/st')
    config.add_route('new_payam','/npayam')
    config.add_route('mnew_payam','/mnpayam')
    config.add_route('ersal_payam','/epayam')
    config.add_route('mersal_payam','/mepayam')
    config.add_route('recive_payam','/rpayam')
    config.add_route('mrecive_payam','/mrpayam')
    config.add_route('new_nameh','/n')
    config.add_route('mnew_nameh','/mn')
    config.add_route('jquery','/url')
    config.add_route('mjquery','/murl')
    config.add_route('ersal_nameh','/ersali')
    config.add_route('mersal_nameh','/mersali')
    config.add_route('edit_nameh','/{id}/edit')
    config.add_route('delet_nameh','/delet')
    config.add_route('delet','/{id}/delet')
    config.add_route('medit_nameh','/{id}/medit')
    config.add_route('view_nameh','/view/{id}')
    config.add_route('mview_nameh','/mview/{id}')
    config.add_route('view_namehu','/{id}/viewu')
    config.add_route('mview_namehu','/{id}/mviewu')
    config.add_route('view_payam','/viewpayam/{id}')
    config.add_route('mview_payam','/mviewpayam/{id}')
    config.add_route('viewu_payam','/viewpayamu/{id}')
    config.add_route('mviewu_payam','/mviewpayamu/{id}')
    config.add_route('kartabl','/nameh')
    config.add_route('mkartabl','/mnameh')
    config.add_route('pishnevis','/pishnevis')
    config.add_route('mpishnevis','/pishnevis')
    config.add_route('imguser','/user/{username}')
    config.add_static_view('deform_static','deform:static/')
    config.add_static_view(name='css',path='tutorial:css')
    config.add_static_view(name='js',path='tutorial:js')
    config.add_static_view(name='img',path='tutorial:images')
    config.add_static_view(name='template',path='tutorial:template')
    config.scan('.views')
    return config.make_wsgi_app()
if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    from pyramid.paster import get_appsettings
    settings = get_appsettings('development.ini')
    server = make_server('0.0.0.0', 5432, main({}, **settings))
    server.serve_forever()