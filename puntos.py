def calcular_puntos(minutos, dia_semana):
	if not isinstance(minutos, int):
		raise ValueError("minutos debe ser entero")
	return 0