"""
Nivel 8: Orquestación del Pipeline Completo
Este módulo contiene la función principal para evaluar expresiones aritméticas de números romanos.
"""

from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida
from calculadora.parser import evaluar_expresion as parsear_expresion


def evaluar(expresion: str) -> int:
    """
    Pipeline completo - Orquestación de todos los niveles.

    Nivel 8: Integrar todo el pipeline de análisis léxico, sintáctico,
    semántico y parsing para evaluar expresiones aritméticas de números romanos.

    Pipeline de compilación:
    1. Análisis Léxico (Nivel 1): Validar alfabeto
    2. Análisis Sintáctico 1 (Nivel 2): Validar repeticiones I/X/C/M
    3. Análisis Sintáctico 2 (Nivel 3): Validar repeticiones V/L/D
    4. Análisis Sintáctico 3 (Nivel 4): Validar orden descendente
    5. Análisis Semántico (Nivel 5): Validar restas válidas
    6. Generación de Código (Nivel 6): Conversión romano→entero
    7. Parsing (Nivel 7): Tokenización y evaluación de expresiones
    8. Orquestación (Nivel 8): Pipeline completo

    💡 PISTA PRIMERO: Llama a parsear_expresion(expresion) para obtener los tokens
    💡 PISTA: Filtra tokens de tipo 'ESPACIO'
    💡 PISTA: Recorre los tokens restantes y aplica las operaciones correspondientes
    💡 PISTA: Al final, valida que el resultado sea positivo (> 0)
    💡 PISTA: Si el resultado es <= 0, lanza ExpresionInvalida con mensaje descriptivo
    💡 PISTA Ejemplo "XIV + LX":
    💡 PISTA:   - Tokens: [ROMANO "XIV", SUMA "+", ROMANO "LX"]
    💡 PISTA:   - romano_a_entero("XIV") = 14 → resultado = 14
    💡 PISTA:   - romano_a_entero("LX") = 60 → resultado = 14 + 60 = 74
    💡 PISTA Ejemplo "X - V":
    💡 PISTA:   - Tokens: [ROMANO "X", RESTA "-", ROMANO "V"]
    💡 PISTA:   - romano_a_entero("X") = 10 → resultado = 10
    💡 PISTA:   - romano_a_entero("V") = 5 → resultado = 10 - 5 = 5
    💡 PISTA Ejemplo "V - X":
    💡 PISTA:   - Tokens: [ROMANO "V", RESTA "-", ROMANO "X"]
    💡 PISTA:   - resultado = 5 - 10 = -5 → lanza ExpresionInvalida


    Args:
        expresion (str): La expresión aritmética a evaluar

    Returns:
        int: El resultado de la expresión

    Raises:
        ExpresionInvalida: Si la expresión tiene errores léxicos, sintácticos o semánticos
        ExpresionInvalida: Si el resultado de la expresión es negativo o cero

    Examples:
        >>> evaluar('XIV + LX')
        74
        >>> evaluar('X - V')
        5
        >>> evaluar('MMMCMXCIX + I')
        4000
    """
    # Obtenemos los tokens de la expresión
    tokens = parsear_expresion(expresion)

    if not tokens:
        raise ExpresionInvalida("La expresión está vacía")

    # Filtramos los espacios para trabajar solo con números y operadores
    tokens_limpios = [t for t in tokens if t.tipo != 'ESPACIO']

    # Inicializamos el resultado con el primer número romano
    resultado = romano_a_entero(tokens_limpios[0].valor)

    # Recorremos los tokens restantes (operador y número)
    i = 1
    while i < len(tokens_limpios):
        operador = tokens_limpios[i].tipo  # "SUMA" o "RESTA"
        siguiente_romano = tokens_limpios[i+1].valor

        valor_siguiente = romano_a_entero(siguiente_romano)

        if operador == "SUMA":
            resultado += valor_siguiente
        elif operador == "RESTA":
            resultado -= valor_siguiente

        i += 2  # Saltamos el operador y el número que acabamos de usar

    # Validación final: Los romanos no tienen resultados <= 0
    if resultado <= 0:
        raise ExpresionInvalida(f"Resultado inválido ({resultado}): Los números romanos deben ser mayores a cero")

    return resultado
