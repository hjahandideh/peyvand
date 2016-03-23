import os

from paste.httpserver import serve


from colander import MappingSchema
from colander import SequenceSchema
from colander import SchemaNode
from colander import String
from colander import Boolean
from colander import Integer
from colander import Length
from colander import OneOf

from deform import ValidationFailure
from deform import Form
from deform import widget


here = os.path.dirname(os.path.abspath(__file__))

colors = (('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'))

class DateSchema(MappingSchema):
    month = SchemaNode(Integer())
    year = SchemaNode(Integer())
    day = SchemaNode(Integer())

class DatesSchema(SequenceSchema):
    date = DateSchema()

class MySchema(MappingSchema):
    name = SchemaNode(String(),
                      description = 'The name of this thing')
    title = SchemaNode(String(),
                       widget = widget.TextInputWidget(size=40),
                       validator = Length(max=20),
                       description = 'A very short title')
    password = SchemaNode(String(),
                          widget = widget.CheckedPasswordWidget(),
                          validator = Length(min=5))
    is_cool = SchemaNode(Boolean(),
                         default = True)
    dates = DatesSchema()
    color = SchemaNode(String(),
                       widget = widget.RadioChoiceWidget(values=colors),
                       validator = OneOf(('red', 'blue')))

def form_view(request):
    schema = MySchema()
    myform = Form(schema, buttons=('submit',))


    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            myform.validate(controls)
        except ValidationFailure as e:
            return {'form':e.render()}
        return {'form':'OK'}
