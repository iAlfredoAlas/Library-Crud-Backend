class RepositoryResponse:
    def __init__(self, content=None, success=True, error_message=None):
        self.content = content
        self.success = success
        self.error_message = error_message
