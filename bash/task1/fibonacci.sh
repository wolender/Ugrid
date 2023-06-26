#!/bin/bash

#The Fibonacci numbers
#[PRACTICAL TASK 1]
#The Fibonacci numbers are the numbers in the following integer sequence.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
#Fn = Fn-1 + Fn-2 with seed values F0 = 0 and F1 = 1.

#Write a function fib that returns Fn. For example, if n = 0, then fib should return 0. If n = 1, then it
#should return 1. For n > 1, it should return Fn-1 + Fn-2

fib() {
    local n=$1
    if [ "$n" -eq "0" ] ; then
        return 0
    
    elif [ "$n" -eq "1" ] ;then
        return 1
    
    else 
        local val1=0
        local val2=0

        fib `expr $n - 1`
        val1=$?
        
        fib `expr $n - 2`
        val2=$?

        return `expr $val1 + $val2`
    fi
}
echo "Please enter N number :"
read n
fib $n
echo $?
