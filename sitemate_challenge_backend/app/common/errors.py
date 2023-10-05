from enum import Enum


class APIErrorCode(str, Enum):
    ISSUE_NOT_FOUND = 'ISSUE_NOT_FOUND'
    ISSUE_TITLE_MISSING = 'ISSUE_TITLE_MISSING'


class PermissionDeniedException(Exception):
    pass


class NotFoundException(Exception):
    pass


class UnprocessableEntityException(Exception):
    pass


class ConflictException(Exception):
    pass


class BadRequestException(Exception):
    pass
