from blocklogger import abrir_os_logs, mostrar_logs

def main():
	with abrir_os_logs() as dados:
		mostrar_logs(dados)
		
if __name__ == '__main__':
	main()
