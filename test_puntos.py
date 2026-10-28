import puntos
import pytest

calcular_puntos = puntos.calcular_puntos

def test_calcular_puntos_falla_recibiendo_string():
	with pytest.raises(ValueError):
		puntos = calcular_puntos("", "martes")