import colander
from pyramid.security import (remember , forget , authenticated_userid)
from .security import USERS
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, forbidden_view_config
from .models import DBSession , Nameh , User
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Userpage ( colander.MappingSchema ):
    name = colander.SchemaNode ( colander.String ( ) )
    lname = colander.SchemaNode ( colander.String ( ) )
    tel = colander.SchemaNode ( colander.Integer ( ) )
    email = colander.SchemaNode ( colander.String ( ) )
    username = colander.SchemaNode ( colander.String ( ) )
    password = colander.SchemaNode ( colander.String ( ) )
    semat = colander.SchemaNode ( colander.String ( ) )
class WikiViews ( object ):
    def __init__(self , request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config ( route_name='nameh' , renderer='nameh_view.pt',permission='view'  )
    def nameh_view(self):
       request=self.request
       newre=DBSession.query(User.username)
       nnameh=""
       mnameh=''
       chnameh=''
       manameh=''
       recive=''
       tarikher=''
       mohlat=''
       jahat=''
       peyvast=''
       if 'form_submitted' in request.params:
            nnameh = request.params['nnameh']
            mnameh = request.params['mnameh']
            chnameh=request.params['chnameh']
            manameh=request.params['manameh']
            recive=request.params['recive']
            ersal=self.logged_in
            tarikher=request.params['tarikher']
            mohlat=request.params['mohlat']
            jahat=request.params['jahat']
            peyvast=request.params['peyvast']

            DBSession.add (Nameh ( nnameh=nnameh , mnameh=mnameh , chnameh=chnameh , manameh=manameh,recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast ) )

            return HTTPFound ( 'n' )

       return dict (newre=newre,nnameh=nnameh,mnameh=mnameh,chnameh=chnameh,manameh=manameh,recive=recive,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast)



    @view_config ( route_name='nameh_page' , renderer='namehpage_view.pt',permission='view' )
    def nameh_page(self):
        id = int ( self.request.matchdict['id'] )
        page = DBSession.query ( Nameh ).filter_by ( id=id ).one ( )
        return dict ( page=page )

    @view_config ( route_name='nameh_view' , renderer='nameh.pt',permission='view' )
    def nameh(self):
        pages =DBSession.query ( Nameh ).filter_by(recive=self.logged_in)
        return dict ( pages=pages )

    @view_config ( route_name='view' , renderer='wiki_view.pt',permission='view' )
    def wiki_view(self):
        if self.logged_in:
            log=DBSession.query(User).filter_by(username=self.logged_in)
            return dict (log=log)

    @view_config(route_name='login', renderer='login.pt')
    @forbidden_view_config(renderer='login.pt')
    def login(self):
       request = self.request
       login_url = request.route_url('login')
       referrer = request.url
       if referrer == login_url:

        referrer = '/username'  # never use login form itself as came_from
        came_from = request.params.get('came_from', referrer)
        message = ''
        login = ''
        password = ''
        if 'form-submitted' in request.params:
            login = request.params['login']
            password = request.params['password']

            if USERS.get(login)==password:

                    headers = remember(request, login)
                    return HTTPFound(location=came_from,
                                 headers=headers)

            message="نام کاربری یا رمز عبور نا معتبر است"
        return dict(
            name='Login',
            message=message,
            url=request.application_url +'/',
            came_from=came_from,
            login=login,
            password=password,

        )
    @view_config(route_name='logout')
    def logout(self):
        request = self.request
        request.authenticated_userid=""
        headers = forget(request)
        url = request.route_url('login')
        return HTTPFound(location=url,
                         headers=headers)


