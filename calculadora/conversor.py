"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""

from calculadora.error import ExpresionInvalida
from calculadora.validaciones import (
    validar_orden_descendente,
    validar_repeticiones_icxm,
    validar_repeticiones_vld,
    validar_restas,
)
from calculadora.validaciones.alfabeto import validar_simbolos


def romano_a_entero(cadena: str) -> int:
    """
    Convierte una cadena de números romanos válida a su valor entero correspondiente.

    Nivel 6: Generación de Código - Conversión Romano → Entero

    💡 PISTA PRIMERO: Llama a todas las validaciones (Niveles 1-5) ANTES de convertir
    💡 PISTA: Usa validar_simbolos(cadena), validar_repeticiones_icxm(cadena), etc.
    💡 PISTA: Si alguna validación retorna False, lanza ExpresionInvalida con mensaje descriptivo (ej: 'contiene símbolos inválidos', 'repetición I/X/C/M', etc.)

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-5

    Returns:
        int: El valor entero correspondiente

    Examples:
        >>> romano_a_entero("I")
        1
        >>> romano_a_entero("V")
        5
        >>> romano_a_entero("IV")
        4
        >>> romano_a_entero("IX")
        9
        >>> romano_a_entero("XIV")
        14
        >>> romano_a_entero("MCMXCIV")
        1994
        >>> romano_a_entero("MMMCMXCIX")
        3999

    Raises:
        ExpresionInvalida: Si la cadena no es válida según las reglas de números romanos (símbolos inválidos, repeticiones inválidas, orden incorrecto, restas inválidas)
    """

    # Si alguna falla, lanzamos el error ExpresionInvalida
    if not validar_simbolos(cadena):
        raise ExpresionInvalida("La expresión contiene símbolos inválidos.")

    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida("La expresión contiene repeticiones inválidas de I, X, C o M.")

    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida("La expresión contiene repeticiones inválidas de V, L o D.")

    if not validar_restas(cadena):
        raise ExpresionInvalida("La expresión contiene restas (sustracciones) inválidas.")

    if not validar_orden_descendente(cadena):
        raise ExpresionInvalida("La expresión no sigue el orden descendente correcto.")

    # LÓGICA DE CONVERSIÓN
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    i = 0
    while i < len(cadena):
        # Valor del símbolo actual
        valor_actual = valores[cadena[i]]

        # Si no es el último símbolo y el siguiente es mayor, es una RESTA
        if i + 1 < len(cadena) and valores[cadena[i+1]] > valor_actual:
            total += (valores[cadena[i+1]] - valor_actual)
            i += 2  # Saltamos los dos símbolos procesados
        else:
            # Si no, simplemente SUMAMOS el valor
            total += valor_actual
            i += 1

    return total
