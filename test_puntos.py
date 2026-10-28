import puntos
import pytest

calcular_puntos = puntos.calcular_puntos

def test_calcular_puntos_falla_recibiendo_puntos_as_string():
	with pytest.raises(ValueError):
		puntos = calcular_puntos("", "martes")

def test_calcular_puntos_falla_recibiendo_dia_not_as_string():
	with pytest.raises(ValueError):
		puntos = calcular_puntos(7.89, 7.89)

def test_calcular_puntos_acepta_flotante():
	puntos = calcular_puntos(5.6, "martes")

def test_viaje_menor_de_diez_minutos_no_da_puntos():
	assert calcular_puntos(9, "martes") == 0