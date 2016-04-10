import colander
import deform.widget
from pyramid.security import (remember , forget , authenticated_userid)
from .security import USERS
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, forbidden_view_config
from .models import DBSession , Page , Nameh , User
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


class WikiPage ( colander.MappingSchema ):
    title = colander.SchemaNode ( colander.String ( ) )
    body = colander.SchemaNode ( colander.String ( ) , widget=deform.widget.RichTextWidget ( ) )


class NamehPage ( colander.MappingSchema ):
    nnameh = colander.SchemaNode ( colander.String ( ) ,
                                   widget=deform.widget.CheckboxWidget ( true_val='ghnh' , false_val='hjgjf' ) )
    mnameh = colander.SchemaNode ( colander.String ( ) )
    chnameh = colander.SchemaNode ( colander.String ( ) , widget=deform.widget.TextAreaWidget ( ) )
    manameh = colander.SchemaNode ( colander.String ( ) , widget=deform.widget.RichTextWidget ( ) )
    recive=colander.SchemaNode(colander.String())
    ersal=colander.SchemaNode(colander.String())
    tarikher=colander.SchemaNode(colander.String())
    mohlat=colander.SchemaNode(colander.String())
    jahat=colander.SchemaNode(colander.String())
    peyvast=colander.SchemaNode(colander.String())





class WikiViews ( object ):
    def __init__(self , request):

        self.request = request
        self.logged_in = request.authenticated_userid
    @property
    def user_form(reqest):
        scem = Userpage ( )
        return deform.Form ( scem , buttons=('submit' ,) )

    @property
    def req(self):
        return self.user_form.get_widget_resources ( )

    @property
    def wiki_form(self):
        schema = WikiPage ( )
        return deform.Form ( schema , buttons=('submit' ,) )

    @property
    def nameh_form(self):
        schem = NamehPage()
        return deform.Form ( schem, buttons=('submit' ,) )

    @property
    def reqt(self):
        return self.nameh_form.get_widget_resources ( )

    @property
    def reqts(self):
        return self.wiki_form.get_widget_resources ( )

    @view_config ( route_name='nameh' , renderer='nameh_view.pt',permission='view'  )
    def nameh_view(self):
        form = self.nameh_form.render ( )
        if 'submit' in self.request.params:
            controls = self.request.POST.items ( )
            try:
                appstruct = self.nameh_form.validate ( controls )
            except deform.ValidationFailure as f:
                # Form is NOT valid
                return dict ( form=f.render ( ) )

            # Add a new page to the database
            if 'widget.checked==true' in self.request.params:
                new_nnameh = 'hjhj'
            else:
                new_nnameh = 'ck'
            new_mnameh = appstruct['mnameh']
            new_chnameh = appstruct['chnameh']
            new_manameh = appstruct['manameh']
            new_recive=appstruct['recive']
            new_ersal=appstruct['ersal']
            new_tarikher=appstruct['tarikher']
            new_mohlat=appstruct['mohlat']
            new_jahat=appstruct['jahat']
            new_peyvast=appstruct['peyvast']

            DBSession.add (
                Nameh ( nnameh=new_nnameh , mnameh=new_mnameh , chnameh=new_chnameh , manameh=new_manameh,recive=new_recive,ersal=new_ersal,tarikher=new_tarikher,mohlat=new_mohlat,jahat=new_jahat,peyvast=new_peyvast ) )

            # Get the new ID and redirect
            page = DBSession.query ( Nameh ).filter_by ( mnameh=new_mnameh ).one ( )
            new_uid = page.id

            url = self.request.route_url ( 'nameh_page' , id=new_uid )
            return HTTPFound ( url )

        return dict ( form=form )



    @view_config ( route_name='nameh_page' , renderer='namehpage_view.pt',permission='view' )
    def nameh_page(self):
        id = int ( self.request.matchdict['id'] )
        page = DBSession.query ( Nameh ).filter_by ( id=id ).one ( )
        return dict ( page=page )

    @view_config ( route_name='nameh_view' , renderer='nameh.pt',permission='view' )
    def nameh(self):
        pages =DBSession.query ( Nameh ).order_by ( Nameh.manameh )
        return dict ( pages=pages )

    @view_config ( route_name='view' , renderer='wiki_view.pt',permission='view' )
    def wiki_view(self):

        if self.logged_in:
            log=DBSession.query(User).filter_by(username=self.logged_in)
        pages = DBSession.query ( Page ).order_by ( Page.title )
        return dict ( title='Wiki View' , pages=pages,log=log)

    @view_config ( route_name='wikipage_add' , renderer='wikipage_addedit.pt',permission='edit'  )
    def wikipage_add(self):
        form = self.wiki_form.render ( )
        if 'submit' in self.request.params:
            controls = self.request.POST.items ( )
            try:
                appstruct = self.wiki_form.validate ( controls )
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict ( form=e.render ( ) )

                # Add a new page to the database
            new_title = appstruct['title']
            new_body = appstruct['body']
            DBSession.add ( Page ( title=new_title , body=new_body ) )

            # Get the new ID and redirect
            page = DBSession.query ( Page ).filter_by ( title=new_title ).one ( )
            new_uid = page.uid

            url = self.request.route_url ( 'wikipage_view' , uid=new_uid )
            return HTTPFound ( url )

        return dict ( form=form )


    @view_config ( route_name='wikipage_view' , renderer='wikipage_view.pt',permission='view' )
    def wikipage_view(self):
        uid = int ( self.request.matchdict['uid'] )
        page = DBSession.query ( Page ).filter_by ( uid=uid ).one ( )
        return dict ( page=page )


    @view_config ( route_name='wikipage_edit' , renderer='wikipage_addedit.pt',permission='edit'  )
    def wikipage_edit(self):
        uid = int ( self.request.matchdict['uid'] )
        page = DBSession.query ( Page ).filter_by ( uid=uid ).one ( )

        wiki_form = self.wiki_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items ( )
            try:
                appstruct = wiki_form.validate ( controls )
            except deform.ValidationFailure as e:
                return dict ( page=page , form=e.render ( ) )

            # Change the content and redirect to the view
            page.title = appstruct['title']
            page.body = appstruct['body']
            url = self.request.route_url ( 'wikipage_view' , uid=uid )
            return HTTPFound ( url )

        form = self.wiki_form.render ( dict ( uid=page.uid , title=page.title , body=page.body ) )

        return dict ( page=page , form=form )
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

            message=USERS
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
        headers = forget(request)
        url = request.route_url('login')
        return HTTPFound(location=url,
                         headers=headers)


