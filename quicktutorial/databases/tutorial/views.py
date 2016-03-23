import colander
import deform.widget

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from .models import DBSession, Page,Nameh


class WikiPage(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())
    body = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.RichTextWidget()
    )
class NamehPage(colander.MappingSchema):
    nnameh=colander.SchemaNode(colander.String())
    mnameh=colander.SchemaNode(colander.String())
    chnameh=colander.SchemaNode(colander.String(),widget=deform.widget.TextAreaWidget())
    manameh=colander.SchemaNode(colander.String(),widget=deform.widget.RichTextWidget())

class WikiViews(object):
    def __init__(self, request):
        self.request = request

    @property
    def wiki_form(self):
        schema = WikiPage()
        return deform.Form(schema, buttons=('submit',))
    @property
    def nameh_form(self):
        schem=NamehPage()
        return deform.Form(schem,buttons=('submit',))
    @property
    def reqt(self):
        return self.nameh_form.get_widget_resources()
    @property
    def reqts(self):
        return self.wiki_form.get_widget_resources()

    @view_config(route_name='nameh', renderer='nameh_view.pt')
    def nameh_view(self):
        form = self.nameh_form.render()
        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.nameh_form.validate(controls)
            except deform.ValidationFailure as f:
                # Form is NOT valid
                return dict(form=f.render())

            # Add a new page to the database
            new_nnameh = appstruct['nnameh']
            new_mnameh = appstruct['mnameh']
            new_chnameh=appstruct['chnameh']
            new_manameh=appstruct['manameh']
            DBSession.add(Nameh(nnameh=new_nnameh,mnameh=new_mnameh,chnameh=new_chnameh,manameh=new_manameh))

            # Get the new ID and redirect
            page = DBSession.query(Nameh).filter_by(mnameh=new_mnameh).one()
            new_uid = page.id

            url = self.request.route_url('nameh_page',id=new_uid)
            return HTTPFound(url)

        return dict(form=form)
    @view_config(route_name='nameh_page',renderer='namehpage_view.pt')
    def nameh_page(self):
        id = int(self.request.matchdict['id'])
        page = DBSession.query(Nameh).filter_by(id=id).one()
        return dict(page=page)
    @view_config(route_name='nameh_view', renderer='nameh.pt')
    def nameh(self):
        pages = DBSession.query(Nameh).order_by(Nameh.manameh)
        return dict( pages=pages)
    @view_config(route_name='wiki_view', renderer='wiki_view.pt')
    def wiki_view(self):
        pages = DBSession.query(Page).order_by(Page.title)
        return dict(title='Wiki View', pages=pages)

    @view_config(route_name='wikipage_add',
                 renderer='wikipage_addedit.pt')
    def wikipage_add(self):
        form = self.wiki_form.render()

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.wiki_form.validate(controls)
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict(form=e.render())

            # Add a new page to the database
            new_title = appstruct['title']
            new_body = appstruct['body']
            DBSession.add(Page(title=new_title, body=new_body))

            # Get the new ID and redirect
            page = DBSession.query(Page).filter_by(title=new_title).one()
            new_uid = page.uid

            url = self.request.route_url('wikipage_view', uid=new_uid)
            return HTTPFound(url)

        return dict(form=form)


    @view_config(route_name='wikipage_view', renderer='wikipage_view.pt')
    def wikipage_view(self):
        uid = int(self.request.matchdict['uid'])
        page = DBSession.query(Page).filter_by(uid=uid).one()
        return dict(page=page)


    @view_config(route_name='wikipage_edit',
                 renderer='wikipage_addedit.pt')
    def wikipage_edit(self):
        uid = int(self.request.matchdict['uid'])
        page = DBSession.query(Page).filter_by(uid=uid).one()

        wiki_form = self.wiki_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = wiki_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(page=page, form=e.render())

            # Change the content and redirect to the view
            page.title = appstruct['title']
            page.body = appstruct['body']
            url = self.request.route_url('wikipage_view', uid=uid)
            return HTTPFound(url)

        form = self.wiki_form.render(dict(
            uid=page.uid, title=page.title, body=page.body)
        )

        return dict(page=page, form=form)