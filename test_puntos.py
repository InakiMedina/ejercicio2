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

def test_puntos_tienen_un_tope_de_veinte():
	assert calcular_puntos(210, 2) == 20

def test_minutos_negativos_lanzan_entrada_invalida():
	with pytest.raises(ValueError, match="^entrada_invalida$"):
		calcular_puntos(-1, 2)

def test_dia_mayor_que_siete_lanza_entrada_invalida():
	with pytest.raises(ValueError, match="^entrada_invalida$"):
		calcular_puntos(10, 8)

def test_calcular_puntos_redondea_hacia_abajo():
	assert calcular_puntos(19.999, "miercoles") == 1