#!/usr/bin/python
import socket,sys,os,requests,urllib

print "--------------------------------------------------------------------------"
print "--------------------------Durandal tool-----------------------------------"
print "--------------------------------------------------------------------------"
print "1. Socket analyser\n2. Banner grabber\n3. Port Scanner\n4. Web analyser\n5. DNS resolver\n"
opcao = raw_input("Digite a opcao: ")
ip = raw_input("Digite o ip: ")

if  (int(opcao) == 1):
	porta = int(input("Digite a porta: "))
	socketarget = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if (socketarget.connect_ex((ip,porta)) == 0):
		print "Status porta",porta,"[Aberta]"
		socketarget.close()

elif (int(opcao) == 2):
	porta = int(input("Digite a porta: "))
	socketarget = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socketarget.connect((ip,porta))
	banner = socketarget.recv(1024)
	print banner

elif (int(opcao) == 3):
	for porta in range(1,65536):
		socketarget = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if (socketarget.connect_ex((ip,porta)) == 0):
			print "Status da porta:",porta,"[Aberta]"
			socketarget.close()

elif (int(opcao) == 4):
	site = requests.get(raw_input("Digite o site com http: "))
	status = site.status_code
	site1 = urllib.urlopen(raw_input("Digite o site de novo com http: "))
	banner = site1.info()
	if (status == 200):
		print "Requisicao",status," e site existente"
		print "O webserver esta rodando\n"
		print banner
	else:
		print "Requisicao",status," e site inexistente"

elif (int(opcao) == 5):
	host = raw_input("Digite o host: ")
	print "----->", socket.gethostbyname(host)
