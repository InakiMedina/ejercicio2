import puntos
import pytest

calcular_puntos = puntos.calcular_puntos

def test_calcular_puntos_falla_recibiendo_puntos_as_string():
	with pytest.raises(ValueError):
		puntos = calcular_puntos("", 2)

def test_calcular_puntos_falla_recibiendo_dia_not_as_string():
	with pytest.raises(ValueError):
		puntos = calcular_puntos(7.89, 7.89)

def test_calcular_puntos_acepta_flotante():
	puntos = calcular_puntos(5.6, 2)

def test_viaje_menor_de_diez_minutos_no_da_puntos():
	assert calcular_puntos(9, 2) == 0

def test_suma_un_punto_por_cada_diez_minutos_completos():
	assert calcular_puntos(25.9, 2) == 2

def test_viaje_de_diez_minutos_en_sabado_duplica_puntos():
	assert calcular_puntos(10, 6) == 2