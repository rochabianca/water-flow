#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import serial
import mysql.connector
comport = serial.Serial('COM7', 9600) #Porta onde está conectado o arduino e velocidade.
print('Serial Iniciada...')             #ATENÇÃO: se o serial monitor estiver sendo usado esse
                                        #código retornará um erro, pois a porta estará em uso

cnx = mysql.connector.connect(user='root', password='', host='localhost', database='waterflow')
cursor = cnx.cursor() 
add_sinais = (
  "INSERT INTO `waterflow`.`sinais` (`sin_id`, `sin_data`, `sin_flow`)" 
  "VALUES (NULL, CURRENT_TIMESTAMP, %(flow)s);"
)

while (True):
    serialValue = comport.readline()
    data_sinais = serialValue
    print(data_sinais)
    cursor.execute(add_sinais,{ 'flow': data_sinais })
    cnx.commit()
    
cursor.close()
cnx.close()
comport.close()