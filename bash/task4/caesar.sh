#!/bin/bash
#use example
#Write caesar cipher script accepting three parameters -s <shift> -i <input file> -o <output file>
# -s <SHIFT_VALUE> -i <INPUT_FILE> -o <OUTPUTFILE> 
while getopts ":s:i:o:" arg; do
  case ${arg} in
    s)    
        SHIFT=$OPTARG
    ;;

    i)
        INPUTFILE=$OPTARG
    ;;

    o)
        OUTPUTFILE=$OPTARG
    ;;

  esac
done

caesarEncrypt (){

  for ((i = 0 ; i <= ${#TEXT}; i++)); do
    CHAR=${TEXT:i:1}

    # Check if the char is a letter

    if [[ $CHAR =~ [a-z] ]]; then

      ASCII_VAL=$(printf "%d" "'$CHAR") #TO ASCII TRANSFORMATION
      END_VAL=$((( ASCII_VAL - 97 + SHIFT ) % 26 + 97))
      END_CHAR=$(printf "\\$(printf %o "$END_VAL")") #TO CHAR TRANSFORMATION

      FINAL_TEXT+=$END_CHAR
    else
      FINAL_TEXT+=$CHAR # if its not a letter dont sypher
    fi

  done

  echo $FINAL_TEXT

}

if [[ -f $INPUTFILE ]]; then
  TEXT=$(<"$INPUTFILE")  
else
  echo "Input file not found."
  exit 1
fi

encrypted_text=$(caesarEncrypt)

echo "$encrypted_text" > $OUTPUTFILE

