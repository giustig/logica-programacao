#!/bin/bash

echo "Digite um número: "
  read  num1
echo "Digite outro número: "
  read  num2

echo "Escolha uma operação:"
echo "1 - Soma"
echo "2 - Subtração"
echo "3 - Multiplicação"
echo "4 - Divisão"
  read op

if [ $op -eq 1 ]; then
  echo "A soma desses números é $[num1+num2]"   
elif [ $op -eq 2 ]; then
  echo "A subtração desses números é $[num1-num2]"    
elif [ $op -eq 3 ]; then
  echo "A multiplicação desses números é $[num1*num2]"   
elif [ $op -eq 4 ]; then
  echo "A divisão desses números é $[num1/num2]"   
else
  echo "Opção inválida."
fi
