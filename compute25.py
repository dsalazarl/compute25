# compute25.py

import re

AVAILABLE_OPERATIONS = ['+','-','*','/']

def is_operation(char: str) -> bool:
	return char in AVAILABLE_OPERATIONS

def is_digit(char: str) -> bool:
	return not is_operation(char)

def postfix_to_infix(postfix_expr: str) -> str:
	infix_expr = []
	for char in postfix_expr:
		if is_digit(char):
			infix_expr.append(char)
		else:
			operand1 = infix_expr.pop()
			operand2 = infix_expr.pop()
			operator = char
			expr = '(' + operand2 + ' ' + operator + ' ' + operand1 + ')' # mejorar con f'({bla}...)'
			infix_expr.append(expr)

	return infix_expr.pop()

def compute25(expr_input: str) -> str:
	'''Descripción de la función'''
	count = 0
	idx_first_digit = list(range(len(expr_input)))
	for idx_1 in idx_first_digit:
		# agregamos primer dígito a la construcción de la expresión
		expr1 = ""
		expr1 += expr_input[idx_1] # expresión con 1 caracter

		# generamos la respectiva lista de posibles índices para los 3 dígitos restantes 
		idx_second_digit = idx_first_digit.copy()
		idx_second_digit.pop(idx_1) # eliminamos el índice del dígito ya usado, para la lista de dígitos restantes
		#print(idx_1, idx_second_digit)

		for i, idx_2 in enumerate(idx_second_digit):
			# agregamos segundo dígito a la construcción de la expresión
			expr2 = expr1
			expr2+=expr_input[idx_2] # expresión con 2 caracteres

			# generamos lista de posible tercer caracter, en este caso correspondería a una operación 
			possible_third_digit = AVAILABLE_OPERATIONS

			# generamos la respectiva lista de posibles índices para los 2 dígitos restantes 
			idx_third_digit = idx_second_digit.copy()
			idx_third_digit.pop(i) # eliminamos el índice del dígito ya usado, para la lista de dígitos restantes

			for operation in possible_third_digit:
				# agregamos primera operación a la construcción de la expresión
				expr3 = expr2
				expr3 += operation # expresión con 3 caracteres
				#print(expr3)

				for i, idx_3 in enumerate(idx_third_digit):
					# agregamos tercer dígito a la construcción de la expresión
					expr4 = expr3
					expr4 += expr_input[idx_3] # expresión con 4 caracteres
					#print(expr4) # 4*3*4*2

					# obtenemos el índices del último dígitos restante
					idx_fourth_digit = idx_third_digit.copy()
					idx_fourth_digit.pop(i) # eliminamos el índice del dígito ya usado, para la lista de dígitos restantes
					idx_fourth_digit = idx_fourth_digit.pop() # sacamos el único índice restante de la lista de índices de dígitos
					fourth_digit = expr_input[idx_fourth_digit]

					# generamos la respectiva lista del posible 5to caracter de la expresión
					# en este punto puede ser una operación o el último dígito aún sin usar
					possible_fifth_char = AVAILABLE_OPERATIONS.copy()
					possible_fifth_char.append(fourth_digit)
					#print(expr4, possible_fifth_char)

					for char5 in possible_fifth_char:
						# agregamos quinto caracter a la construcción de la expresión
						expr5 = expr4
						expr5 += char5

						# a partir de aquí, 2 posibilidades: viene operación y luego dígito, o viene dígito y luego operación
						#possible_sixth_char = []
						if is_operation(char5):
							# si viene operación, a continuación sigue el último dígito y finalmente, la última operación
							possible_sixth_char = [fourth_digit]
						else:
							# si viene dígito, a continuación sigue la penúltima operación y finalmente, la última operación
							possible_sixth_char = AVAILABLE_OPERATIONS.copy()


						for char6 in possible_sixth_char:
							# agregamos sexto caracter a la construcción de la expresión
							expr6 = expr5
							expr6 += char6

							# en este punto, las últimas opciones para el séptimo caracter corresponden a una operación +-*/
							possible_seventh_char = AVAILABLE_OPERATIONS.copy()

							for char7 in possible_seventh_char:
								# agregamos sexto caracter a la construcción de la expresión
								expr7 = expr6
								expr7 += char7

								count += 1
								#print(count, expr7, postfix_to_infix(expr7), eval(postfix_to_infix(expr7)))
								infix_expr = postfix_to_infix(expr7)
								if eval(infix_expr)==25:
									print(f'Se probaron {count} combinaciones para encontrar la expresión: {infix_expr}')
									return infix_expr


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
