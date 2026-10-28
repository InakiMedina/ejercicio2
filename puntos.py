def calcular_puntos(minutos, dia_semana):
	if not isinstance(minutos, (int, float)):
		raise ValueError("entrada_invalida")

	if minutos < 0:
		raise ValueError("entrada_invalida")
	
	if type(dia_semana) is not int or not 1 <= dia_semana <= 7:
		raise ValueError("entrada_invalida")

	puntos = int(minutos // 10)
	if dia_semana in (6, 7):
		puntos *= 2
	return min(puntos, 20)