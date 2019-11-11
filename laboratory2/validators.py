from re import match

def getInt( text ):

    num = input( text )

    while not bool( match( r'^[-+]{0,1}\d+$', num ) ):
        num = input( text )

    return int( num )

def getFloat( text ):

    num = input( text )

    while not bool( match( r'^[-+]{0,1}\d+[.]?\d*$', num ) ):
        num = input( text )

    return float( num )