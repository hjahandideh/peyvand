import colander
import deform.widget
from pyramid.response import Response
from pyramid.security import (remember , forget , authenticated_userid)
from .security import USERS
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, forbidden_view_config
from .models import DBSession , Nameh , User,Paygham,payam,Image
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
    @view_config ( route_name='edit_nameh' , renderer='template/edit_nameh.pt',permission='view' )
    def nameh_edit(self):

       log=DBSession.query(User).filter_by(username=self.logged_in)
       page=DBSession.query(Paygham).all()
       request=self.request
       newre=DBSession.query(User.username)
       nnameh=""
       mnameh=''
       chnameh=''
       manameh=''
       recive=''
       ersal=''
       tarikher=''
       mohlat=''
       jahat=''
       peyvast=''
       st=''
       if 'form_submitted' in request.params:
            nnameh = request.params['nnameh']
            mnameh = request.params['mnameh']
            chnameh=request.params['chnameh']
            manameh=request.params['manameh']
            recive=request.params['recive']
            if recive=="":
                ersal=""
            else:
                ersal=self.logged_in
            tarikher=request.params['tarikher']
            mohlat=request.params['mohlat']
            jahat=request.params['jahat']
            peyvast=request.params['peyvast']
            st=request.params['st']



            DBSession.add (Nameh ( nnameh=nnameh , mnameh=mnameh , chnameh=chnameh , manameh=manameh,
                                   recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,st=st ) )

            return HTTPFound ( 'n' )

       return dict (newre=newre,nnameh=nnameh,mnameh=mnameh,chnameh=chnameh,manameh=manameh,recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,st=st,log=log,page=page)

    @view_config ( route_name='new_nameh' , renderer='template/new_nameh.pt',permission='view' )
    def nameh_view(self):
       log=DBSession.query(User).filter_by(username=self.logged_in)
       page=DBSession.query(Paygham).all()
       request=self.request
       newre=DBSession.query(User.username)
       nnameh=""
       mnameh=''
       chnameh=''
       manameh=''
       recive=''
       ersal=''
       tarikher=''
       mohlat=''
       jahat=''
       peyvast=''
       st=''
       if 'form_submitted' in request.params:
            nnameh = request.params['nnameh']
            mnameh = request.params['mnameh']
            chnameh=request.params['chnameh']
            manameh=request.params['manameh']
            recive=request.params['recive']
            if recive=="":
                ersal=""
            else:
                ersal=self.logged_in
            tarikher=request.params['tarikher']
            mohlat=request.params['mohlat']
            jahat=request.params['jahat']
            peyvast=request.params['peyvast']
            st=request.params['st']



            DBSession.add (Nameh ( nnameh=nnameh , mnameh=mnameh , chnameh=chnameh , manameh=manameh,
                                   recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,st=st ) )

            return HTTPFound ( 'n' )

       return dict (newre=newre,nnameh=nnameh,mnameh=mnameh,chnameh=chnameh,manameh=manameh,recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,st=st,log=log,page=page)
    @view_config ( route_name='user' , renderer='template/user.pt',permission='view' )
    def user_view(self):
       log=DBSession.query(User).filter_by(username=self.logged_in)
       page=DBSession.query(Paygham).all()
       request=self.request

       name=''
       lname=''
       tel=''
       email=''
       username=''
       password=''
       semat=''
       if 'form-user' in request.params:
            new_name = request.params['fname']
            new_lname = request.params['lname']
            new_tel=request.params['tel']
            new_email=request.params['email']
            new_username=request.params['username']
            new_password=request.params['password']
            new_semat=request.params['semat']
            DBSession.add (User ( name=new_name,lname=new_lname,tel=new_tel,email=new_email,username=new_username,password=new_password,semat=new_semat))
            url=self.request.route_url('imguser',id=new_username)
            return HTTPFound (url)
       return dict(log=log,page=page,name=name,lname=lname,tel=tel,email=email,username=username,password=password,semat=semat)
    @view_config ( route_name='imguser' , renderer='template/imguser.pt',permission='view' )
    def imguser(self):


        if 'photo.submitted' in self.request.params:
            input_file = self.request.POST['file_input'].file
            tmp = '../static/images/%s' % (DBSession.query(Image).order_by(Image.id).first().id + 1)
            open(tmp, 'w').write(input_file.read())

    @view_config(route_name='generate_ajax_data', renderer='json',permission='view')                     #1
    def my_ajax_view(request):                                                         #2
        return {'message': "yo mamma's so classless she could be a marxist utopia"}
    @view_config ( route_name='view' , renderer='template/view.pt',permission='view' )
    def wiki_view(self):
        request=self.request
        mpayam=''
        if 'frm-submitted' in request.params:
            mpayam=request.params['mpayam']
            ersal=self.logged_in
            DBSession.add(Paygham(mpayam=mpayam,ersal=ersal))
            return HTTPFound('username')
        log=DBSession.query(User).filter_by(username=self.logged_in)
        mag=DBSession.query(Image).filter_by(name=self.logged_in)
        page=DBSession.query(Paygham).all()
        return dict (log=log,mag=mag,page=page,mpayam=mpayam)

                       #1

    @view_config ( route_name='ersal_nameh' , renderer='template/ersal_nameh.pt',permission='view' )
    def ernameh(self):
            log=DBSession.query(User).filter_by(username=self.logged_in)
            usr=DBSession.query(Nameh).filter_by(ersal=self.logged_in)
            page=DBSession.query(Paygham).all()
            return dict (log=log,page=page,usr=usr)


    @view_config ( route_name='kartabl' , renderer='template/kartabl.pt',permission='view' )
    def kartabl(self):
        if self.logged_in:
            log=DBSession.query(User).filter_by(username=self.logged_in)
            usr=DBSession.query(Nameh).filter_by(recive=self.logged_in)
            page=DBSession.query(Paygham).all()
            return dict (log=log,page=page,usr=usr)


    @view_config ( route_name='pishnevis' , renderer='template/pishnevis.pt',permission='view' )
    def pishnevis(self):
        if self.logged_in:
            log=DBSession.query(User).filter_by(username=self.logged_in)
            usr=DBSession.query(Nameh).filter_by(recive="")
            page=DBSession.query(Paygham).all()
            return dict (log=log,page=page,usr=usr)

    @view_config ( route_name='eghdam' , renderer='template/eghdam.pt',permission='view' )
    def eghdam(self):
        if self.logged_in:
            log=DBSession.query(User).filter_by(username=self.logged_in)
            page=DBSession.query(Paygham).all()
            return dict (log=log,page=page)

    @view_config ( route_name='new_payam' , renderer='template/new_payam.pt',permission='view' )
    def new_payam(self):
        request=self.request
        mpayam=''
        mopayam=''
        ersal=''
        recive=''
        if 'frm-submit' in request.params:
            mpayam=request.params['mpayam']
            mopayam=request.params['mopayam']
            ersal=self.logged_in
            recive=request.params['recive']
            DBSession.add(payam(mapyam=mpayam,mopyam=mopayam,ersal=ersal,recive=recive))
            return HTTPFound('npayam')
        log=DBSession.query(User).filter_by(username=self.logged_in)
        page=DBSession.query(Paygham).all()
        return dict (log=log,page=page,mpayam=mpayam,mopayam=mopayam,ersal=ersal,recive=recive)

    @view_config ( route_name='ersal_payam' , renderer='template/ersal_payam.pt',permission='view' )
    def ersal_payam(self):
        if self.logged_in:
            log=DBSession.query(User).filter_by(username=self.logged_in)
            page=DBSession.query(Paygham).all()
            return dict (log=log,page=page)

    @view_config ( route_name='recive_payam' , renderer='template/recive_payam.pt',permission='view' )
    def recive_payam(self):
        if self.logged_in:
            log=DBSession.query(User).filter_by(username=self.logged_in)
            page=DBSession.query(Paygham).all()
            return dict (log=log,page=page)

    @view_config ( route_name='save' , renderer='template/save.pt',permission='view' )
    def save(self):
        if self.logged_in:
            log=DBSession.query(User).filter_by(username=self.logged_in)
            page=DBSession.query(Paygham).all()
            return dict (log=log,page=page)

    @view_config ( route_name='search' , renderer='template/search.pt',permission='view' )
    def search(self):
        if self.logged_in:
            log=DBSession.query(User).filter_by(username=self.logged_in)
            page=DBSession.query(Paygham).all()
            return dict (log=log,page=page)

    @view_config(route_name='login', renderer='template/login.pt')
    @forbidden_view_config(renderer='template/login.pt')
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


