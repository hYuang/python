from ctypes import *

class barley_amount(Union):
    _fields_=[
        ('barley_long',c_long),
        ('barley_int',c_int),
        ('barley_char',c_char*8),
    ]
value=raw_input("Enter thevalue")
my_barley=barley_amount(int(value))
print  "%s" % my_barley.barley_char