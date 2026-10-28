def calcular_puntos(minutos, dia_semana):
	if not isinstance(minutos, float):
		raise ValueError("minutos debe ser flotante")
	
	if not isinstance(dia_semana, str):
		raise ValueError("minutos debe ser una cadena de texto")
	return 0