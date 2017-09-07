import string

values = {'var':'foo'}

t = string.Template("""
    Variable : $var
    Escape   : $$
    Variable in text ; ${var}iable
""")

s ="""
    Variable : %(var)s
    Escape   : %%
    Variable in text : %(var)siable
"""

print 'TEMPLATE: ',t.substitute(values)

print 'INTERPOLATION: ',s %  values

