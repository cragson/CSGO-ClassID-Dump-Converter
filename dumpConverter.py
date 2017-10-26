#   CSGO sv_dump_class_info converter
#
#           written by cragson
#
#   < ! > do the fuck you want license < ! >
#
#   < x > Do not punch me for my skills in python. I agree I am a big noob < x >

from os import system

def getDump( FILENAME ):
    
    tempDump = []

    found_ak = False # Yes forgive me this might be a dirty workaround
                     # but I don't care. It's a run only once program.
    
    with open( FILENAME, 'r' ) as file: # Opening the file

        for line in file: # Self-explaining
            
            line = ''.join( line.split() ) # Removing all space before and after the string

            if( found_ak == False ): # Checking if found the ak string yet because at AK the class IDs starts
                if( ( "CAK47" in line ) == True ):  # if we found it 
                    found_ak = True
                else:                # else we skipping the lines before
                    continue 
            
            tempDump.append( line )  # appending our temporary list the line                            

    file.close() 

    return tempDump # returning now the final list

def convertDump( DUMP ):

    convDump = []

    idNumber = 1 # Class ID representive integer
    
    for element in DUMP: # for every 'element' in the list we format it so we can c+p in vs/ whatever
        
        convDump.append( str( element.split('(')[ 0 ] + " = " + str( idNumber ) ) + "," )

        idNumber += 1 # ClassID 1up

    return convDump

            
def printDump( DUMP ):
    
    print("\n < ~ > Converted Dump < ~ > \n\n")
    
    print( "enum ClassIDs" )
    print("{")
    
    for classID in range( 0, len( DUMP ) - 1, 1 ):

        print( "\t" + str( DUMP[ classID ] ) )

    print( "};\n" )

def main():
    
    print("================================")
    print("   CSGO ClassID Dump Converter  ")
    print("\n\n written by cragson\n\n     ")

    print(" Enter the name of the file which contains the dump.\n ")
    print(" You can get the dump from csgo with sv_dump_class_info.\n ")
    print(" [ ! ] MUST  BE  IN  SAME  LOCATION  AS  THE  CONVERTER [ ! ]\n\n ")
    print(" usage < filename > " )
    print("\n Example usage : csgo-dump.txt ")
    filename = input( "\n\t" )
    
    if( filename != ' ' ):
        FinalDump = getDump( filename )

    RawDump = getDump( filename )

    ConvertedDump = convertDump( RawDump )
    
    printDump( ConvertedDump )

    system("pause") # ugly

if __name__ == '__main__':
    main()
