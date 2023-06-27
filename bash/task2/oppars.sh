#!/bin/bash
#sequence of numbers task

# [PRACTICAL TASK 2]

# Write bash script accepting operation parameter (“-”, “+”, “*”, “%”), sequence of numbers and debug flag.

# For example:

# ./your_script.sh -o % -n 5 3 -d

# Result: 2

# ./your_script.sh -o + -n 3 5 7 -d

# Result: 15  
#use example
# -d for debug -o <OPERATOR> -n <NUMBER NUMBER NUMBER ...>

print_debug_info() {
  echo "User: $USER"
  echo "Script: $0"
  echo "Operation: $operator"
  echo "Numbers: ${#numbers[@]}"
}
debug=0
numbers=()
i=0
for arg in "$@"; do
  case $arg in
    -d)
        debug=1
        shift
        ;;
    -o)
        shift 
        operator=$1
        ;;
    *)
      if [[ $arg =~ [0-9] ]]; then
        numbers+=($arg)
        shift
      else
        shift
      fi
      ;;

  esac
done

echo ${numbers[@]}
if [[ $operator == * ]]; then #works for * as a parameter
  operator='*'
fi
if [ $debug -eq 1 ]; then
    print_debug_info
fi  

result=${numbers[0]}
case $operator in
  -)
    for ((i = 1; i < ${#numbers[@]}; i++)); do
      result=$((result - numbers[i]))
    done
    ;;
  +)
    for ((i = 1; i < ${#numbers[@]}; i++)); do
      result=$((result + numbers[i]))
    done
    ;;
  \*)
    for ((i = 1; i < ${#numbers[@]}; i++)); do
      result=$((result * numbers[i]))
    done
    ;;
  %)
    for ((i = 1; i < ${#numbers[@]}; i++)); do
      result=$((result % numbers[i]))
    done
    ;;

esac

echo "The ressult is : $result"