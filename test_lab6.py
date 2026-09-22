import pytest

from lab6 import (
    calcular_imc,
    categorizar_imc,
    classificar_pessoa,
    classificar_vento,
    tem_frete_gratis,
)


@pytest.mark.parametrize(
    ("imc", "esperado"),
    [
        (18.49, "abaixo do peso"),
        (18.5, "peso normal"),
        (18.51, "peso normal"),
        (24.99, "peso normal"),
        (25, "sobrepeso"),
        (25.01, "sobrepeso"),
        (29.99, "sobrepeso"),
        (30, "obesidade"),
        (30.01, "obesidade"),
    ],
    ids=[
        "18_5-abaixo",
        "18_5-exato",
        "18_5-acima",
        "25-abaixo",
        "25-exato",
        "25-acima",
        "30-abaixo",
        "30-exato",
        "30-acima",
    ],
)
def test_categorizar_imc_cobre_fronteiras(imc, esperado):
    assert categorizar_imc(imc) == esperado


@pytest.mark.parametrize(
    ("peso", "altura", "esperado"),
    [
        (50, 2, "abaixo do peso"),
        (70, 1.75, "peso normal"),
        (70, 1.6, "sobrepeso"),
        (100, 1.6, "obesidade"),
    ],
    ids=["abaixo-do-peso", "peso-normal", "sobrepeso", "obesidade"],
)
def test_classificar_pessoa_representa_classes(peso, altura, esperado):
    assert classificar_pessoa(peso, altura) == esperado


@pytest.mark.parametrize("peso, altura", [(0, 1.7), (70, 0)])
def test_calcular_imc_rejeita_valores_nao_positivos(peso, altura):
    with pytest.raises(ValueError):
        calcular_imc(peso, altura)


@pytest.mark.parametrize(
    ("velocidade", "esperado"),
    [
        (19.99, "calmo"),
        (20, "moderado"),
        (20.01, "moderado"),
        (39.99, "moderado"),
        (40, "forte"),
        (40.01, "forte"),
        (59.99, "forte"),
        (60, "tempestade"),
        (60.01, "tempestade"),
    ],
    ids=[
        "20-abaixo",
        "20-exato",
        "20-acima",
        "40-abaixo",
        "40-exato",
        "40-acima",
        "60-abaixo",
        "60-exato",
        "60-acima",
    ],
)
def test_classificar_vento_cobre_fronteiras(velocidade, esperado):
    assert classificar_vento(velocidade) == esperado


@pytest.mark.parametrize(
    ("valor_compra", "cliente_premium", "peso", "esperado"),
    [
        (199.99, False, 30.01, False),
        (199.99, False, 30, False),
        (199.99, True, 30.01, False),
        (199.99, True, 30, False),
        (200, False, 30.01, False),
        (200, False, 30, False),
        (200, True, 30.01, False),
        (200, True, 30, True),
    ],
    ids=["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"],
)
def test_tabela_de_decisao_frete(
    valor_compra, cliente_premium, peso, esperado
):
    assert tem_frete_gratis(valor_compra, cliente_premium, peso) is esperado