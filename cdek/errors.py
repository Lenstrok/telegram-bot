
class CdekError(Exception):
    """Базовая ошибка клиента cdek."""
    pass


class CdekLocationError(CdekError):
    """Ошибка получения локации cdek."""
    pass


class CdekAuthError(CdekError):
    """Оштбка аутентификации cdek."""
    pass
