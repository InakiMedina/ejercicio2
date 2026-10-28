def calcular_puntos(minutos, dia_semana):
	if not isinstance(minutos, (int, float)):
		raise ValueError("minutos debe ser numérico")
	
	if not isinstance(dia_semana, str):
		raise ValueError("minutos debe ser una cadena de texto")
	return int(minutos // 10)