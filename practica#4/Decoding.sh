#Decodificando ambas imagenes
base64 --decode mystery_img1.txt > mystery1.png
base64 --decode mystery_img2.txt > mystery2.png
#codificando el mensaje
base64 hola_mundo.c > mensaje.txt