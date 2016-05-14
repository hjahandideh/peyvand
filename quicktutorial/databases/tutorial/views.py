import os
import shutil

from pyramid.security import (remember , forget , authenticated_userid)
from tutorial.security import USERS
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, forbidden_view_config
from .models import DBSession , Nameh , User,Paygham,payam,Image,etela
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class WikiViews ( object ):
  def __init__(self , request):
        self.request = request
        self.logged_in = request.authenticated_userid
  @view_config ( route_name='edit_nameh' , renderer='template/nameh_edit.pt',permission='view' )
  def nameh_edit(self):
       n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
       id =int(self.request.matchdict['id'])
       page = DBSession.query(Nameh).filter_by(id=id).one()
       log=DBSession.query(User).filter_by(username=self.logged_in)
       mag=DBSession.query(Image).filter_by(name=self.logged_in)
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
            if ersal=="":
                vaseiyat=self.logged_in
            else:
                vaseiyat="F"



            DBSession.add (Nameh ( nnameh=nnameh , mnameh=mnameh , chnameh=chnameh , manameh=manameh,
                                   recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,vaseiyat=vaseiyat ) )

            return HTTPFound ( 'ersali' )

       return dict (page=page,nav=n,mag=mag,newre=newre,nnameh=nnameh,mnameh=mnameh,chnameh=chnameh,manameh=manameh,recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,vaseiyat=vaseiyat,log=log)
  @view_config ( route_name='new_nameh' , renderer='template/new_nameh.pt',permission='view' )
  def nameh_view(self):
       n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
       log=DBSession.query(User).filter_by(username=self.logged_in)
       mag=DBSession.query(Image).filter_by(name=self.logged_in)
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
            if ersal=="":
                vaseiyat=self.logged_in
            else:
                vaseiyat="F"



            DBSession.add (Nameh ( nnameh=nnameh , mnameh=mnameh , chnameh=chnameh , manameh=manameh,
                                   recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,vaseiyat=vaseiyat ) )

            return HTTPFound ( 'ersali' )

       return dict (nav=n,mag=mag,newre=newre,nnameh=nnameh,mnameh=mnameh,chnameh=chnameh,manameh=manameh,recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,vaseiyat=vaseiyat,log=log)

  @view_config ( route_name='imguser' , renderer='template/imguser.pt',permission='view' )
  def store_mp3_view(self):
    # ``filename`` contains the name of the file in string format.
    mag=DBSession.query(Image).filter_by(name=self.logged_in)
    log=DBSession.query(User).filter_by(username=self.logged_in)
    n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
    id =self.request.matchdict['username']
    request=self.request
    if "frmimg" in request.params:
      filename = request.POST['mp3'].filename
      filename1 = request.POST['emza'].filename
      input_file = request.POST['mp3'].file
      input_file1 = request.POST['emza'].file

      x="emza"+id+".jpg"
      x1=id+".jpg"
      file_path = os.path.join('../databases/tutorial/images/user/',x1)
      file_path1 = os.path.join('../databases/tutorial/images/emza',x)
      y="tutorial:images/"+x;
      y1="tutorial:images/"+x1;
      DBSession.add(Image(name=id,img=y))
      DBSession.add(Image(name=id,img=y1))
      temp_file_path = file_path + '~'
      temp_file_path1 = file_path1 + '~'
      input_file.seek(0)
      input_file1.seek(0)
      with open(temp_file_path, 'wb') as output_file:
            shutil.copyfileobj(input_file, output_file)
      os.rename(temp_file_path, file_path)
      with open(temp_file_path1, 'wb') as output_file1:
            shutil.copyfileobj(input_file1, output_file1)
      os.rename(temp_file_path1, file_path1)
      return HTTPFound('/username')
    return dict(mag=mag,log=log,nav=n)
  @view_config ( route_name='user' , renderer='template/user.pt',permission='view' )
  def user_view(self):
       log=DBSession.query(User).filter_by(username=self.logged_in)
       mag=DBSession.query(Image).filter_by(name=self.logged_in)
       n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
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
       return dict(log=log,mag=mag,name=name,lname=lname,tel=tel,email=email,username=username,password=password,semat=semat,nav=n)

  @view_config ( route_name='view' , renderer='template/view.pt',permission='view' )
  def wiki_view(self):
    log=DBSession.query(User).filter_by(username=self.logged_in)
    mag=DBSession.query(Image).filter_by(name=self.logged_in)
    n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
    et=DBSession.query(etela).all()
    namehr=DBSession.query(Nameh).filter_by(recive=self.logged_in).count()
    namehe=DBSession.query(Nameh).filter_by(ersal=self.logged_in).count()
    pag=DBSession.query(Paygham).all()
    return dict (log=log,pag=pag,mag=mag,nav=n,namehe=namehe,namehr=namehr,et=et)


  @view_config(route_name='jquery', renderer='json')
  def second_function(self):
    request=self.request
    if "frm-submitted" in request.params:
        mpayam=request.params['mpayam']
        ersal=self.logged_in

        y="<img  class='imgsize1' src='http://localhost:8080/img/"+ersal+".jpg'>"

        DBSession.add(Paygham(mpayam=mpayam,ersal=ersal,img=y))
        page=DBSession.query(Paygham).all()

        ls = []
        for i in page:

            ls.append(dict(id=i.id, mpayam=i.mpayam, ersal=i.ersal,img=i.img))
        return dict(page=ls)

  @view_config(route_name='view_nameh', renderer='template/view_nameh.pt')
  def view_nameh(self):
        mag=DBSession.query(Image).filter_by(name=self.logged_in)
        n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        log=DBSession.query(User).filter_by(username=self.logged_in)
        id = int(self.request.matchdict['id'])
        pag = DBSession.query(Nameh).filter_by(id=id).one()
        pag.vaseiyat="T"
        page=DBSession.query(Nameh).filter_by(id=id)

        return dict(page=page,log=log,mag=mag,nav=n,vaseiyat=pag.vaseiyat)
  @view_config(route_name='view_namehu', renderer='template/view_namehu.pt')
  def view_namehu(self):
        mag=DBSession.query(Image).filter_by(name=self.logged_in)
        n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        log=DBSession.query(User).filter_by(username=self.logged_in)
        id = int(self.request.matchdict['id'])
        page=DBSession.query(Nameh).filter_by(id=id)
        return dict(page=page,log=log,mag=mag,nav=n)
  @view_config ( route_name='ersal_nameh' , renderer='template/ersal_nameh.pt',permission='view' )
  def ernameh(self):
        log=DBSession.query(User).filter_by(username=self.logged_in)
        n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        mag=DBSession.query(Image).filter_by(name=self.logged_in)
        usr=DBSession.query(Nameh).filter_by(ersal=self.logged_in)
        return dict (log=log,usr=usr,mag=mag,nav=n)

  @view_config ( route_name='kartabl' , renderer='template/kartabl.pt',permission='view' )
  def kartabl(self):
     n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
     mag=DBSession.query(Image).filter_by(name=self.logged_in)
     log=DBSession.query(User).filter_by(username=self.logged_in)
     usr=DBSession.query(Nameh).filter_by(recive=self.logged_in)
     return dict (log=log,usr=usr,mag=mag,nav=n)
  @view_config ( route_name='pishnevis' , renderer='template/pishnevis.pt',permission='view' )
  def pishnevis(self):
            mag=DBSession.query(Image).filter_by(name=self.logged_in)
            n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            log=DBSession.query(User).filter_by(username=self.logged_in)
            usr=DBSession.query(Nameh).filter_by(vaseiyat=self.logged_in)
            return dict (log=log,usr=usr,mag=mag,nav=n)
  @view_config ( route_name='eghdam' , renderer='template/eghdam.pt',permission='view' )
  def eghdam(self):
            mag=DBSession.query(Image).filter_by(name=self.logged_in)
            n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            log=DBSession.query(User).filter_by(username=self.logged_in)
            return dict (log=log,mag=mag,nav=n)
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
        mag=DBSession.query(Image).filter_by(name=self.logged_in)
        n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        page=DBSession.query(Paygham).all()
        return dict (log=log,mag=mag,page=page,mpayam=mpayam,mopayam=mopayam,ersal=ersal,recive=recive,nav=n)
  @view_config ( route_name='ersal_payam' , renderer='template/ersal_payam.pt',permission='view' )
  def ersal_payam(self):
            n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            mag=DBSession.query(Image).filter_by(name=self.logged_in)
            log=DBSession.query(User).filter_by(username=self.logged_in)
            dpayam=DBSession.query(payam).filter_by(ersal=self.logged_in)
            return dict (log=log,dpayam=dpayam,mag=mag,nav=n)
  @view_config ( route_name='recive_payam' , renderer='template/recive_payam.pt',permission='view' )
  def recive_payam(self):
            n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            mag=DBSession.query(Image).filter_by(name=self.logged_in)
            log=DBSession.query(User).filter_by(username=self.logged_in)
            dpayam=DBSession.query(payam).filter_by(recive=self.logged_in)

            return dict (log=log,dpayam=dpayam,mag=mag,nav=n)
  @view_config ( route_name='save' , renderer='template/save.pt',permission='view' )
  def save(self):
            mag=DBSession.query(Image).filter_by(name=self.logged_in)
            n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            log=DBSession.query(User).filter_by(username=self.logged_in)
            return dict (log=log,mag=mag,nav=n)
  @view_config ( route_name='search' , renderer='template/search.pt',permission='view' )
  def search(self):
            mag=DBSession.query(Image).filter_by(name=self.logged_in)
            n=DBSession.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            log=DBSession.query(User).filter_by(username=self.logged_in)
            return dict (log=log,mag=mag,nav=n)
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


