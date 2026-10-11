class AIError(Exception):
    pass


class AIConnectionError(AIError):
    pass


class AITimeoutError(AIError):
    pass


class AIResponseError(AIError):
    pass