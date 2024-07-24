# excepciones.py

class UsuarioError(Exception):
    """Excepción base para errores relacionados con usuarios."""
    pass

class UsuarioInvalidoError(UsuarioError):
    """Excepción para cuando un usuario tiene datos inválidos."""
    pass

class UsuarioNoEncontradoError(UsuarioError):
    """Excepción para cuando un usuario no es encontrado."""
    pass
