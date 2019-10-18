#renovador de ip interno
#salve com o nome renew.py
#va no cmd e entre no msm diretorio e digite "renew.py conexao" (sem aspas) [conexao é um argumento para o programa executar uma #determinada ação]
import sys
import os
import time
argumento=sys.argv
time.sleep(3)
def conexao():
    print("\nrenovador de ip Interno V.1.1")
    time.sleep(3)
    c= os.system("ipconfig /flushdns")
    x= os.system("ipconfig /release")
    y= os.system("ipconfig /renew")
    m= os.system("cls")
    return c,x,y,m
    time.sleep(1)
if argumento[1] == "conexao":
    conexao()
    print("\n Ip renovado")
    time.sleep(30)

