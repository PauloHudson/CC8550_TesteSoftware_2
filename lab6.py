 """Implementacao dos exercicios do Laboratorio 6 de CC8550."""

from math import inf


def calcular_imc(peso, altura):
    """Calcula o IMC e rejeita peso ou altura nao positivos."""
    if peso <= 0 or altura <= 0:
        raise ValueError("peso e altura devem ser positivos")
    return peso / altura**2


def classificar_por_faixas(valor, faixas):
    """Retorna o rotulo da primeira faixa cujo limite superior nao e excedido."""
    for limite_superior, rotulo in faixas:
        if valor < limite_superior:
            return rotulo
    raise ValueError("as faixas devem terminar com um limite superior adequado")


FAIXAS_IMC = (
    (18.5, "abaixo do peso"),
    (25, "peso normal"),
    (30, "sobrepeso"),
    (inf, "obesidade"),
)

FAIXAS_VENTO = (
    (20, "calmo"),
    (40, "moderado"),
    (60, "forte"),
    (inf, "tempestade"),
)


def categorizar_imc(imc):
    return classificar_por_faixas(imc, FAIXAS_IMC)


def classificar_pessoa(peso, altura):
    return categorizar_imc(calcular_imc(peso, altura))


def classificar_vento(velocidade):
    return classificar_por_faixas(velocidade, FAIXAS_VENTO)


def tem_frete_gratis(valor_compra, cliente_premium, peso):
    """Frete gratis exige que as tres condicoes sejam verdadeiras."""
    return valor_compra >= 200 and cliente_premium and peso <= 30