import os
import shutil
from datetime import date, datetime

from pyramid.security import (remember , forget, authenticated_userid)
from pyramid.url import route_url

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, forbidden_view_config
from .models import Session , Nameh , User,Paygham,payam,Image,etela,Vorood, Groups,Delet_Nameh
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()





class WikiViews ( object ):
  def __init__(self , request):
        self.request = request
        userid = authenticated_userid(self.request)
        usernam = Session.query(User.username).filter_by(id=userid)
        self.logged_in =usernam

  @view_config ( route_name='edit_nameh' , renderer='template/nameh_edit.pt',permission='entry' )
  def nameh_edit(self):
       n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
       id =int(self.request.matchdict['id'])
       page = Session.query(Nameh).filter_by(id=id).one()
       log=Session.query(User).filter_by(username=self.logged_in)
       payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
       mag=Session.query(Image).filter_by(name=self.logged_in)
       request=self.request
       newre=Session.query(User.username)
       if 'form_submitted' in request.params:
            page.nnameh = request.params['nnameh']
            page.mnameh = request.params['mnameh']
            page.chnameh=request.params['chnameh']
            page.manameh=request.params['manameh']
            page.recive=request.params['recive']
            if page.recive=="":
                page.ersal=""
            else:
                page.ersal=request.params['ersal']
            page.tarikher=datetime.now()
            page.mohlat=request.params['mohlat']
            page.jahat=request.params['jahat']
            page.peyvast=request.params['peyvast']

            if page.ersal=="":
                page.vaseiyat=request.params['ersal']
            else:
                page.vaseiyat="F"

            return HTTPFound ( '/pishnevis' )

       return dict( nav=n,log=log,mag=mag,newre=newre,id=page.id,nnameh=page.nnameh , mnameh=page.mnameh , chnameh=page.chnameh , manameh=page.manameh,recive=page.recive,ersal=page.ersal,tarikher=page.tarikher,mohlat=page.mohlat,jahat=page.jahat,peyvast=page.peyvast,vaseiyat=page.vaseiyat )
  @view_config ( route_name='delet' , renderer='template/delet_nameh.pt',permission='entry' )
  def nameh_delet(self):
       id = int(self.request.matchdict['id'])
       page=Session.query(Nameh).filter_by(id=id).one()
       Session.add(Delet_Nameh(nnameh=page.nnameh , mnameh=page.mnameh , chnameh=page.chnameh , manameh=page.manameh,ersal=page.ersal,tarikher=page.tarikher,mohlat=page.mohlat,jahat=page.jahat,peyvast=page.peyvast,vaseiyat=page.vaseiyat ))
       Session.delete(page)
       n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
       page1=Session.query(Delet_Nameh).all()
       log=Session.query(User).filter_by(username=self.logged_in)
       mag=Session.query(Image).filter_by(name=self.logged_in)
       newre=Session.query(User.username)



       return dict( nav=n,log=log,mag=mag,newre=newre,page=page1)
  @view_config ( route_name='new_nameh' , renderer='template/new_nameh.pt',permission='entry' )
  def nameh_view(self):
       n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
       payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
       log=Session.query(User).filter_by(username=self.logged_in)
       mag=Session.query(Image).filter_by(name=self.logged_in)
       request=self.request
       newre=Session.query(User.username)
       if 'form_submitted' in request.params:
            nnameh = request.params['nnameh']
            mnameh = request.params['mnameh']
            chnameh=request.params['chnameh']
            manameh=request.params['manameh']
            recive=request.params['recive']
            if recive=="":
                ersal=""
            else:
                ersal=request.params['ersal']
            tarikher=datetime.now()
            mohlat=request.params['mohlat']
            emza="<img  class='imgsize' src='http://localhost:8080/img/emza/emza"+request.params['ersal']+".jpg'>"
            jahat=request.params['jahat']
            peyvast=request.params['peyvast']
            if ersal=="":
                vaseiyat=request.params['ersal']
            else:
                vaseiyat="F"



            Session.add (Nameh ( nnameh=nnameh , mnameh=mnameh , chnameh=chnameh , manameh=manameh,
                                   recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,emza=emza,jahat=jahat,peyvast=peyvast,vaseiyat=vaseiyat ) )

            return HTTPFound ( 'ersali' )

       return dict (nav=n,mag=mag,newre=newre,log=log)


  @view_config ( route_name='view' , renderer='template/view.pt',permission='entry' )
  def wiki_view(self):
    log=Session.query(User).filter_by(username=self.logged_in)
    mag=Session.query(Image).filter_by(name=self.logged_in)
    n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
    et=Session.query(etela).all()
    namehr=Session.query(Nameh).filter_by(recive=self.logged_in).count()
    namehe=Session.query(Nameh).filter_by(ersal=self.logged_in).count()
    payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
    pag=Session.query(Paygham).all()
    return dict (log=log,pag=pag,mag=mag,nav=n,namehe=namehe,namehr=namehr,et=et,payamr=payamr)

  @view_config(route_name='jquery', renderer='json')
  def second_function(self):
    if "frm-submitted" in self.request.params:
        mpayam=self.request.params['mpayam']

        ersal=self.request.params['ersal']
        dat=datetime.now()
        y="<img  class='imgsize1' src='http://localhost:8080/img/user/"+ersal+".jpg'>"
        Session.add(Paygham(mpayam=mpayam,ersal=ersal,img=y,dat=dat))
        page=Session.query(Paygham).all()
        ls = []
        for i in page:
            ls.append(dict(id=i.id, mpayam=i.mpayam, ersal=i.ersal,img=i.img))
        return dict(page=ls)
  @view_config(route_name='view_payam', renderer='template/view_payam.pt',permission='entry' )
  def view_payam(self):
        mag=Session.query(Image).filter_by(name=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        p=Session.query(payam).filter_by(state="0").count()
        log=Session.query(User).filter_by(username=self.logged_in)
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        id = int(self.request.matchdict['id'])

        page=Session.query(payam).filter_by(id=id)

        return dict(page=page,log=log,mag=mag,nav=n,nam=p)
  @view_config(route_name='viewu_payam', renderer='template/viewu_payam.pt',permission='entry' )
  def viewu_payam(self):
        mag=Session.query(Image).filter_by(name=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        p=Session.query(payam).filter_by(state="0").count()
        log=Session.query(User).filter_by(username=self.logged_in)
        id = int(self.request.matchdict['id'])
        pag = Session.query(payam).filter_by(id=id).one()
        pag.state="1"
        page=Session.query(payam).filter_by(id=id)

        return dict(page=page,log=log,mag=mag,nav=n,state=pag.state,nam=p)
  @view_config(route_name='view_nameh', renderer='template/view_nameh.pt',permission='entry' )
  def view_nameh(self):
        mag=Session.query(Image).filter_by(name=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        log=Session.query(User).filter_by(username=self.logged_in)
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        id = int(self.request.matchdict['id'])
        pag = Session.query(Nameh).filter_by(id=id).one()
        pag.vaseiyat="T"
        page=Session.query(Nameh).filter_by(id=id)

        return dict(page=page,log=log,mag=mag,nav=n,vaseiyat=pag.vaseiyat)
  @view_config(route_name='view_namehu', renderer='template/view_namehu.pt',permission='entry' )
  def view_namehu(self):
        mag=Session.query(Image).filter_by(name=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        log=Session.query(User).filter_by(username=self.logged_in)
        id = int(self.request.matchdict['id'])
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        page=Session.query(Nameh).filter_by(id=id)
        return dict(page=page,log=log,mag=mag,nav=n)
  @view_config ( route_name='ersal_nameh' , renderer='template/ersal_nameh.pt',permission='entry'  )
  def ernameh(self):
        log=Session.query(User).filter_by(username=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        mag=Session.query(Image).filter_by(name=self.logged_in)
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        usr=Session.query(Nameh).filter_by(ersal=self.logged_in)
        return dict (log=log,usr=usr,mag=mag,nav=n)

  @view_config ( route_name='kartabl' , renderer='template/kartabl.pt',permission='entry'  )
  def kartabl(self):
     n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
     mag=Session.query(Image).filter_by(name=self.logged_in)
     log=Session.query(User).filter_by(username=self.logged_in)
     payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
     usr=Session.query(Nameh).filter_by(recive=self.logged_in)

     return dict (log=log,usr=usr,mag=mag,nav=n)
  @view_config ( route_name='pishnevis' , renderer='template/pishnevis.pt',permission='entry'  )
  def pishnevis(self):
            mag=Session.query(Image).filter_by(name=self.logged_in)
            n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            log=Session.query(User).filter_by(username=self.logged_in)
            payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
            usr=Session.query(Nameh).filter_by(vaseiyat=self.logged_in)
            return dict (log=log,usr=usr,mag=mag,nav=n)

  @view_config ( route_name='new_payam' , renderer='template/new_payam.pt',permission='entry'  )
  def new_payam(self):

        request=self.request
        if 'frm-submit' in request.params:
            mpayam=request.params['mpayam']
            mopayam=request.params['mopayam']
            ersal=request.params['ersal']
            state=0
            recive=request.params['recive']
            Session.add(payam(mapyam=mpayam,mopyam=mopayam,ersal=ersal,recive=recive,state=state))
            return HTTPFound('npayam')
        log=Session.query(User).filter_by(username=self.logged_in)
        mag=Session.query(Image).filter_by(name=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        page=Session.query(Paygham).all()
        return dict (log=log,mag=mag,page=page,nav=n)
  @view_config ( route_name='ersal_payam' , renderer='template/ersal_payam.pt',permission='entry'  )
  def ersal_payam(self):
            n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            mag=Session.query(Image).filter_by(name=self.logged_in)
            log=Session.query(User).filter_by(username=self.logged_in)
            payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
            dpayam=Session.query(payam).filter_by(ersal=self.logged_in)
            return dict (log=log,dpayam=dpayam,mag=mag,nav=n)
  @view_config ( route_name='recive_payam' , renderer='template/recive_payam.pt',permission='entry' )
  def recive_payam(self):
            n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            mag=Session.query(Image).filter_by(name=self.logged_in)
            payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
            log=Session.query(User).filter_by(username=self.logged_in)
            dpayam=Session.query(payam).filter_by(recive=self.logged_in)

            return dict (log=log,dpayam=dpayam,mag=mag,nav=n)
  @view_config ( route_name='new_etla' , renderer='template/new_etla.pt',permission='entry'  )
  def new_etla(self):

        request=self.request
        if 'frm-etla' in request.params:
            title=request.params['title']
            etla=request.params['etla']
            Session.add(etela(title=title,etla=etla))
            return HTTPFound('')
        log=Session.query(User).filter_by(username=self.logged_in)
        mag=Session.query(Image).filter_by(name=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        page=Session.query(Paygham).all()
        return dict (log=log,mag=mag,page=page,nav=n)
  # admin
  @view_config ( route_name='medit_nameh' , renderer='template/m_nameh_edit.pt',permission='topsecret' )
  def mnameh_edit(self):
       n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
       id =int(self.request.matchdict['id'])
       page = Session.query(Nameh).filter_by(id=id).one()
       payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
       log=Session.query(User).filter_by(username=self.logged_in)
       mag=Session.query(Image).filter_by(name=self.logged_in)
       request=self.request
       newre=Session.query(User.username)
       if 'form_submitted' in request.params:
            page.nnameh = request.params['nnameh']
            page.mnameh = request.params['mnameh']
            page.chnameh=request.params['chnameh']
            page.manameh=request.params['manameh']
            page.recive=request.params['recive']
            if page.recive=="":
                page.ersal=""
            else:
                page.ersal=request.params['ersal']
            page.tarikher=datetime.now()
            page.mohlat=request.params['mohlat']
            page.jahat=request.params['jahat']
            page.peyvast=request.params['peyvast']
            if page.ersal=="":
                page.vaseiyat=request.params['ersal']
            else:
                page.vaseiyat="F"

            return HTTPFound ( '/pishnevis' )

       return dict( nav=n,log=log,mag=mag,newre=newre,id=page.id,nnameh=page.nnameh , mnameh=page.mnameh , chnameh=page.chnameh , manameh=page.manameh,recive=page.recive,ersal=page.ersal,tarikher=page.tarikher,mohlat=page.mohlat,jahat=page.jahat,peyvast=page.peyvast,vaseiyat=page.vaseiyat )

  @view_config ( route_name='mnew_nameh' , renderer='template/m_new_nameh.pt',permission='topsecret' )
  def mnameh_view(self):
       n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
       log=Session.query(User).filter_by(username=self.logged_in)
       payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
       mag=Session.query(Image).filter_by(name=self.logged_in)
       request=self.request
       newre=Session.query(User.username)
       if 'form_submitted' in request.params:
            nnameh = request.params['nnameh']
            mnameh = request.params['mnameh']
            chnameh=request.params['chnameh']
            manameh=request.params['manameh']
            recive=request.params['recive']
            if recive=="":
                ersal=""
            else:
                ersal=request.params['ersal']
            tarikher=datetime.now()
            mohlat=request.params['mohlat']
            jahat=request.params['jahat']
            peyvast=request.params['peyvast']
            if ersal=="":
                vaseiyat=request.params['ersal']
            else:
                vaseiyat="F"



            Session.add (Nameh ( nnameh=nnameh , mnameh=mnameh , chnameh=chnameh , manameh=manameh,
                                   recive=recive,ersal=ersal,tarikher=tarikher,mohlat=mohlat,jahat=jahat,peyvast=peyvast,vaseiyat=vaseiyat ) )

            return HTTPFound ( 'ersali' )

       return dict (nav=n,mag=mag,newre=newre,log=log)
  @view_config ( route_name='imguser' , renderer='template/imguser.pt',permission='entry' )
  def mimg_view(self):
    # ``filename`` contains the name of the file in string format.
    mag=Session.query(Image).filter_by(name=self.logged_in)
    payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
    log=Session.query(User).filter_by(username=self.logged_in)
    n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
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
      file_path1 = os.path.join('../databases/tutorial/images/emza/',x)
      y="tutorial:images/emza/"+x;
      y1="tutorial:images/user/"+x1;
      Session.add(Image(name="emza"+id,img=y))
      Session.add(Image(name=id,img=y1))
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


  @view_config ( route_name='user' , renderer='template/user.pt',permission='entry' )
  def user_add(self):
       log=Session.query(User).filter_by(username=self.logged_in)
       mag=Session.query(Image).filter_by(name=self.logged_in)
       payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
       n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
       request=self.request
       if 'form-user' in request.params:
            new_name = request.params['fname']
            new_lname = request.params['lname']
            new_tel=request.params['tel']
            new_email=request.params['email']
            new_username=request.params['username']
            new_password=request.params['password']
            new_semat=request.params['semat']
            Session.add (User ( name=new_name,lname=new_lname,tel=new_tel,email=new_email,username=new_username,password=new_password,semat=new_semat))
            url = self.request.route_url('imguser',username=new_username)
            return HTTPFound (url)
       return dict(log=log,mag=mag,nav=n)

  @view_config ( route_name='modir' , renderer='template/modir.pt',permission='topsecret' )
  def modir_view(self):
    log=Session.query(User).filter_by(username=self.logged_in)
    mag=Session.query(Image).filter_by(name=self.logged_in)
    n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
    et=Session.query(etela).all()
    namehr=Session.query(Nameh).filter_by(recive=self.logged_in).count()
    namehe=Session.query(Nameh).filter_by(ersal=self.logged_in).count()
    payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
    pag=Session.query(Paygham).all()
    return dict (log=log,pag=pag,mag=mag,nav=n,namehe=namehe,namehr=namehr,et=et)

  @view_config(route_name='mjquery', renderer='json')
  def msecond_function(self):
    if "frm-submitted" in self.request.params:
        mpayam=self.request.params['mpayam']

        ersal=self.request.params['ersal']
        dat=datetime.now()
        y="<img  class='imgsize1' src='http://localhost:8080/img/user/"+ersal+".jpg'>"
        Session.add(Paygham(mpayam=mpayam,ersal=ersal,img=y,dat=dat))
        page=Session.query(Paygham).all()
        ls = []
        for i in page:
            ls.append(dict(id=i.id, mpayam=i.mpayam, ersal=i.ersal,img=i.img))
        return dict(page=ls)
  @view_config(route_name='mview_payam', renderer='template/m_view_payam.pt',permission='topsecret' )
  def mview_payam(self):
        mag=Session.query(Image).filter_by(name=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        p=Session.query(payam).filter_by(state="0").count()
        log=Session.query(User).filter_by(username=self.logged_in)
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        id = int(self.request.matchdict['id'])

        page=Session.query(payam).filter_by(id=id)

        return dict(page=page,log=log,mag=mag,nav=n,nam=p,payamr=payamr)
  @view_config(route_name='mviewu_payam', renderer='template/m_viewu_payam.pt',permission='topsecret' )
  def mviewu_payam(self):
        mag=Session.query(Image).filter_by(name=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        p=Session.query(payam).filter_by(state="0").count()
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        log=Session.query(User).filter_by(username=self.logged_in)
        id = int(self.request.matchdict['id'])
        pag = Session.query(payam).filter_by(id=id).one()
        pag.state="1"
        page=Session.query(payam).filter_by(id=id)

        return dict(page=page,log=log,mag=mag,nav=n,state=pag.state,nam=p,payamr=payamr)
  @view_config(route_name='mview_nameh', renderer='template/m_view_nameh.pt',permission='topsecret' )
  def mview_nameh(self):
        mag=Session.query(Image).filter_by(name=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        log=Session.query(User).filter_by(username=self.logged_in)
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        id = int(self.request.matchdict['id'])
        pag = Session.query(Nameh).filter_by(id=id).one()
        pag.vaseiyat="T"
        page=Session.query(Nameh).filter_by(id=id)

        return dict(page=page,log=log,mag=mag,nav=n,vaseiyat=pag.vaseiyat,payamr=payamr)
  @view_config(route_name='mview_namehu', renderer='template/m_view_namehu.pt',permission='topsecret' )
  def mview_namehu(self):
        mag=Session.query(Image).filter_by(name=self.logged_in)
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        log=Session.query(User).filter_by(username=self.logged_in)
        id = int(self.request.matchdict['id'])
        page=Session.query(Nameh).filter_by(id=id)
        return dict(page=page,log=log,mag=mag,nav=n,payamr=payamr)
  @view_config ( route_name='mersal_nameh' , renderer='template/m_ersal_nameh.pt',permission='topsecret'  )
  def mernameh(self):
        log=Session.query(User).filter_by(username=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        mag=Session.query(Image).filter_by(name=self.logged_in)
        usr=Session.query(Nameh).filter_by(ersal=self.logged_in)
        return dict (log=log,usr=usr,mag=mag,nav=n,payamr=payamr)

  @view_config ( route_name='mkartabl' , renderer='template/m_kartabl.pt',permission='topsecret'  )
  def mkartabl(self):
     n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
     mag=Session.query(Image).filter_by(name=self.logged_in)
     payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
     log=Session.query(User).filter_by(username=self.logged_in)
     usr=Session.query(Nameh).filter_by(recive=self.logged_in)
     return dict (log=log,usr=usr,mag=mag,nav=n,payamr=payamr)
  @view_config ( route_name='mpishnevis' , renderer='template/m_pishnevis.pt',permission='topsecret'  )
  def mpishnevis(self):
            mag=Session.query(Image).filter_by(name=self.logged_in)
            n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
            log=Session.query(User).filter_by(username=self.logged_in)
            usr=Session.query(Nameh).filter_by(vaseiyat=self.logged_in)
            return dict (log=log,usr=usr,mag=mag,nav=n,payamr=payamr)

  @view_config ( route_name='mnew_payam' , renderer='template/m_new_payam.pt',permission='topsecret'  )
  def mnew_payam(self):

        request=self.request
        if 'frm-submit' in request.params:
            mpayam=request.params['mpayam']
            mopayam=request.params['mopayam']
            ersal=request.params['ersal']
            state=0
            recive=request.params['recive']
            Session.add(payam(mapyam=mpayam,mopyam=mopayam,ersal=ersal,recive=recive,state=state))
            return HTTPFound('npayam')
        log=Session.query(User).filter_by(username=self.logged_in)
        mag=Session.query(Image).filter_by(name=self.logged_in)
        n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
        payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
        page=Session.query(Paygham).all()
        return dict (log=log,mag=mag,page=page,nav=n,payamr=payamr)
  @view_config ( route_name='mersal_payam' , renderer='template/m_ersal_payam.pt',permission='topsecret'  )
  def mersal_payam(self):
            n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            mag=Session.query(Image).filter_by(name=self.logged_in)
            payamr=Session.query(payam).filter_by(recive=self.logged_in).count()
            log=Session.query(User).filter_by(username=self.logged_in)
            dpayam=Session.query(payam).filter_by(ersal=self.logged_in)
            return dict (log=log,dpayam=dpayam,mag=mag,nav=n,payamr=payamr)
  @view_config ( route_name='mrecive_payam' , renderer='template/m_recive_payam.pt',permission='topsecret' )
  def mrecive_payam(self):
            n=Session.query(Nameh).filter_by(recive=self.logged_in, vaseiyat="F").count()
            mag=Session.query(Image).filter_by(name=self.logged_in)
            log=Session.query(User).filter_by(username=self.logged_in)
            dpayam=Session.query(payam).filter_by(recive=self.logged_in)
            payamr=Session.query(payam).filter_by(recive=self.logged_in).count()

            return dict (log=log,dpayam=dpayam,mag=mag,nav=n,payamr=payamr)

  #login
  @view_config(route_name='login', renderer='template/login.pt')
  @forbidden_view_config(renderer='template/login.pt')
  def login(self):
        if 'form-submitted' in self.request.params:
            login = self.request.params['login']
            password = self.request.params['password']
            user = User.by_username(login)
            if user and user.validate_password(password):
                dat=datetime.now()
                Session.add(Vorood(vorod=login,dat=dat))
                headers = remember(self.request, user.id)
                home = route_url('view', self.request)
                return HTTPFound(location=home, headers=headers)

            message = 'Please check your username or password'
            return dict(message=message, login=login, password=password)
        else:
            return {'login':'', 'password':'', 'message':''}
  @view_config(route_name='logout')
  def logout(self):
        headers = forget(self.request)
        loginpage = route_url('login', self.request)
        return HTTPFound(location=loginpage, headers=headers)


