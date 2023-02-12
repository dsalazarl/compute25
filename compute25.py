# compute25.py

import re

def compute25(expr_input: str) -> str:
	'''Descripción de la función'''
	return "SIN SOLUCIÓN"


if __name__ == "__main__":
	running = True
	while running:
		str_in = input("\nIngrese número de 4 dígitos <\"fin\"> para terminar:\n")
		if str_in == "fin" or str_in == "FIN":
			print("Ejecución terminada. Adiós!")
			running = False
		else:
			if bool(re.match("^\d{4}$", str_in)):
				print(compute25(str_in))
			else:
				print("Formato incorrecto!\n")
