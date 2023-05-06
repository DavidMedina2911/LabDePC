#!/bin/bash

mensaje="hola mundo"
echo $mensaje

#condicional if 

nombre="martha"
echo $nombre

if [[ $nombre =~ (.*)a$ ]]
then
    echo Sra. $nombre
else
    echo Sr. $nombre
fi

#ciclo for 

for (( i=10; i<20; i++ ))
do
 echo $i
done