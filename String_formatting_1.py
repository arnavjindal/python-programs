# source - https://realpython.com/python-input-output/#the-string-modulo-operator


'''
d, i, u	Decimal integer
x, X	Hexadecimal integer
o	Octal integer
f, F	Floating point
e, E	Exponential
g, G	Floating point or Exponential
c	Single character
s, r, a	String
%	Single '%' character
'''



'%x, %X' % (252, 252)



'fc, FC'
'%o' % 16
'20'


print(f"{3.14:><20F} { 3.14:10.2f}")


print('%e, %E' % (1000.0, 1000.0))
# prints -'1.000000e+03, 1.000000E+03'


# The g and G conversion types choose between floating point or exponential output, depending on the magnitude of the exponent

print('%g' % 3.14)
# '3.14'

print('%g' % 0.00000003)
# '3e-08'

print('%G' % 0.00000003)
# '3E-08'



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deep Dive: inf and NaN
# Under some circumstances, a floating-point operation can result in a value that is essentially infinite. The string representation of such a number in Python is 'inf'.
#
# It also may happen that a floating-point operation produces a value that is not representable as a number. Python represents this with the string 'NaN'.
#
# When these values are converted with the string modulo operator, the conversion type character controls the case of the resulting output. f and e produce lowercase output, while F and E produce uppercase:

x = float('NaN')
print('%f, %e, %F, %E' % (x, x, x, x))
'nan, nan, NAN, NAN'
y = float('Inf')
print('%f, %e, %F, %E' % (y, y, y, y))
'inf, inf, INF, INF'
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# '%*d' % (5, 123)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# >>> '%#o' % 16
# '0o20'
#
# >>> '%#x' % 16, '%#X' % 16
# ('0x10', '0X10')
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# >>> '%.0f' % 123
# '123'
# >>> '%#.0f' % 123
# '123.'
#
# >>> '%.0e' % 123
# '1e+02'
# >>> '%#.0e' % 123
# '1.e+02'


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# >>> '%-5d' % 123
# '123  '
#
# >>> '%-8.2f' % 123.3
# '123.30  '
#
# >>> '%-*s' % (10, 'foo')
# 'foo       '
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The + and ' ' Flags
# >>> '%+d' % 3
# '+3'
# >>> '%+5d' % 3
# '   +3'
# >>> '% d' % 3
# ' 3'
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# >>> d = {'quantity': 6, 'item': 'bananas', 'price': 1.74}
#
# >>> '%(quantity)d %(item)s cost $%(price).2f' % d
# '6 bananas cost $1.74'
#
# >>> 'It will cost you $%(price).2f for %(item)s, if you buy %(quantity)d' % d
# 'It will cost you $1.74 for bananas, if you buy 6'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 'Get %d%% off on %s today only!' % (30, 'bananas')
# 'Get 30% off on bananas today only!'
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






























































