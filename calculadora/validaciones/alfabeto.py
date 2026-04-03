"""
Nivel 1: Análisis Léxico - Alfabeto (Σ = {I, V, X, L, C, D, M})
"""

def validar_simbolos(cadena: str) -> bool:
    """
    Valida si todos los caracteres de la cadena pertenecen al alfabeto romano.

    💡 PISTA: Usa .strip() para eliminar espacios en blanco laterales
    💡 PISTA: Retorna False si la cadena está vacía después de eliminar espacios
    💡 PISTA: Recuerda: espacios en blanco laterales NO deben afectar la validación

    Args:
        cadena (str): La cadena a evaluar. Ej: "XIV"

    Returns:
        bool: True si la cadena es completamente válida, False en caso contrario.

    Examples:
        >>> validar_simbolos("XIV")
        True
        >>> validar_simbolos("MCMXCIV")
        True
        >>> validar_simbolos("ABCD")
        False
        >>> validar_simbolos("X-IV")
        False
        >>> validar_simbolos("")
        False
        >>> validar_simbolos("  XIV  ")
        True
    """
    cadena_limpia = cadena.strip()

    if not cadena_limpia:
        return False

    alfabeto_romano = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}

    return all(caracter in alfabeto_romano for caracter in cadena_limpia)
