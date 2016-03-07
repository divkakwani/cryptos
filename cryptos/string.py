"""
This module contains string operations used in cryptology.

@author  : Divyanshu Kakwani <divkakwani@gmail.com>
@license : MIT
"""


"""
string <-> num translation functions
"""
def chr2bin(c): return format(ord(c), 'b').zfill(8)
def str2bin(s): return chr2bin(s[0]) + (str2bin(s[1:]) if len(s) > 1 else '')
def str2num(s): return int(str2bin(s), base=2)
def num2str(n): return (num2str(n//256) if n >= 256 else '') + chr(n%256)




