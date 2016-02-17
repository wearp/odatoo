class ValidationError(Exception):
    pass


class RecordValidationError(ValidationError):
    pass


class FieldValidationError(ValidationError):
    pass
