from ctypes import *
msvcrt =cdll.msvcrt
message_string = "hello huang "
msvcrt.printf("Testing : %s",message_string)