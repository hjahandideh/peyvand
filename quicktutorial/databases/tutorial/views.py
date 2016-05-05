import os
import shutil

from pyramid.security import (remember , forget , authenticated_userid)
from tutorial.security import USERS
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, forbidden_view_config
from .models import DBSession , Nameh , User,Paygham,payam,Image
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

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
            vaseiyat=request.params['vaseiyat']



            DBSession.add (Nameh ( nnameh=nnameh , mnameh=mnameh , chnameh=chnameh , manameh=manameh,
                                   recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,vaseiyat=vaseiyat ) )

            return HTTPFound ( 'n' )

       return dict (newre=newre,nnameh=nnameh,mnameh=mnameh,chnameh=chnameh,manameh=manameh,recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,st=st,log=log,page=page)
  @view_config ( route_name='new_nameh' , renderer='template/new_nameh.pt',permission='view' )
  def nameh_view(self):
       log=DBSession.query(User).filter_by(username=self.logged_in)

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
       vaseiyat=''
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
            vaseiyat=0



            DBSession.add (Nameh ( nnameh=nnameh , mnameh=mnameh , chnameh=chnameh , manameh=manameh,
                                   recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,vaseiyat=vaseiyat ) )

            return HTTPFound ( 'n' )

       return dict (newre=newre,nnameh=nnameh,mnameh=mnameh,chnameh=chnameh,manameh=manameh,recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,vaseiyat=vaseiyat,log=log)
  @view_config ( route_name='imguser' , renderer='template/imguser.pt',permission='view' )
  def store_mp3_view(self):
    # ``filename`` contains the name of the file in string format.
    id =self.request.matchdict['username']
    request=self.request
    # WARNING: this example does not deal with the fact that IE sends an
    # absolute file *path* as the filename.  This example is naive; it
    # trusts user input.
    if "frmimg" in request.params:
        filename = request.POST['mp3'].filename

    # ``input_file`` contains the actual file data which needs to be
    # stored somewhere.

        input_file = request.POST['mp3'].file

    # Note that we are generating our own filename instead of trusting
    # the incoming filename since that might result in insecure paths.
    # Please note that in a real application you would not use /tmp,
    # and if you write to an untrusted location you will need to do
    # some extra work to prevent symlink attacks.
        x=id+".jpg"
        file_path = os.path.join('../databases/tutorial/images',x)
        y="tutorial:images/"+x;
        DBSession.add(Image(name=id,img=y))
    # We first write to a temporary file to prevent incomplete files from
    # being used.

        temp_file_path = file_path + '~'

    # Finally write the data to a temporary file
        input_file.seek(0)
        with open(temp_file_path, 'wb') as output_file:
            shutil.copyfileobj(input_file, output_file)

    # Now that we know the file has been fully saved to disk move it into place.

        os.rename(temp_file_path, file_path)

        return HTTPFound('/username')
    return {}
  @view_config ( route_name='user' , renderer='template/user.pt',permission='view' )
  def user_view(self):
       log=DBSession.query(User).filter_by(username=self.logged_in)
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
            url = self.request.route_url('imguser',username=new_username)
            return HTTPFound (url)
       return dict(log=log,name=name,lname=lname,tel=tel,email=email,username=username,password=password,semat=semat)

  @view_config ( route_name='view' , renderer='template/view.pt',permission='view' )
  def wiki_view(self):
    log=DBSession.query(User).filter_by(username=self.logged_in)
    pag=DBSession.query(Paygham).all()
    mag=DBSession.query(Image).filter_by(name=self.logged_in)
    return dict (log=log,pag=pag,mag=mag)


  @view_config(route_name='jquery', renderer='json')
  def second_function(self):
    request=self.request
    if "frm-submitted" in request.params:
        mpayam=request.params['mpayam']
        ersal=self.logged_in
        DBSession.add(Paygham(mpayam=mpayam,ersal=ersal))
        page=DBSession.query(Paygham).all()
        ls = []
        for i in page:
            ls.append(dict(id=i.id, mpayam=i.mpayam, ersal=i.ersal))
        return dict(page=ls)

  @view_config(route_name='view_nameh', renderer='template/view_nameh.pt')
  def view_nameh(self):
        log=DBSession.query(User).filter_by(username=self.logged_in)
        id = int(self.request.matchdict['id'])
        ghg = DBSession.query(Nameh).filter_by(id=id).one()


        return dict(ghg=ghg,log=log)
  @view_config ( route_name='ersal_nameh' , renderer='template/ersal_nameh.pt',permission='view' )
  def ernameh(self):
        log=DBSession.query(User).filter_by(username=self.logged_in)
        usr=DBSession.query(Nameh).filter_by(ersal=self.logged_in)
        return dict (log=log,usr=usr)

  @view_config ( route_name='kartabl' , renderer='template/kartabl.pt',permission='view' )
  def kartabl(self):

     log=DBSession.query(User).filter_by(username=self.logged_in)
     usr=DBSession.query(Nameh).filter_by(recive=self.logged_in)
     return dict (log=log,usr=usr)
  @view_config ( route_name='pishnevis' , renderer='template/pishnevis.pt',permission='view' )
  def pishnevis(self):
            log=DBSession.query(User).filter_by(username=self.logged_in)
            usr=DBSession.query(Nameh).filter_by(ersal="")
            return dict (log=log,usr=usr)
  @view_config ( route_name='eghdam' , renderer='template/eghdam.pt',permission='view' )
  def eghdam(self):
            log=DBSession.query(User).filter_by(username=self.logged_in)
            return dict (log=log)
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
            log=DBSession.query(User).filter_by(username=self.logged_in)
            return dict (log=log)
  @view_config ( route_name='recive_payam' , renderer='template/recive_payam.pt',permission='view' )
  def recive_payam(self):
            log=DBSession.query(User).filter_by(username=self.logged_in)
            return dict (log=log)
  @view_config ( route_name='save' , renderer='template/save.pt',permission='view' )
  def save(self):
            log=DBSession.query(User).filter_by(username=self.logged_in)
            return dict (log=log)
  @view_config ( route_name='search' , renderer='template/search.pt',permission='view' )
  def search(self):
            log=DBSession.query(User).filter_by(username=self.logged_in)
            return dict (log=log)
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


