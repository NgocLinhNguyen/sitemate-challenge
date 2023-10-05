from app.databases.models.issue import Issue
from app.databases.session import session_scope
from app.databases.services.base import BaseService
from app.common.errors import (
    NotFoundException, APIErrorCode, BadRequestException
)


class IssueService(BaseService):
    def __init__(self, session):
        self.session = session
        self.model = Issue

    def create_issue(
            self, title, description=None, auto_close=False
    ):
        if not title:
            raise BadRequestException(APIErrorCode.ISSUE_TITLE_MISSING)
        with session_scope(self.session, auto_close=auto_close):
            new_issue = self.create(title=title, description=description)
        self.session.refresh(new_issue)
        return new_issue

    def list_issues(self, limit=10, offset=0):
        return self.index(limit=limit, offset=offset)[1]

    def get_issue_detail(self, issue_id):
        issue_obj = self.first(id=issue_id)
        if not issue_obj:
            raise NotFoundException(APIErrorCode.ISSUE_NOT_FOUND)
        return issue_obj

    def update_issue(
            self, issue_id, title=None, description=None, auto_close=False
    ):
        issue_obj = self.get_issue_detail(issue_id)
        update_info = {}
        if title is not None:
            update_info['title'] = title
        if description is not None:
            update_info['description'] = description

        if update_info:
            with session_scope(self.session, auto_close=auto_close):
                issue_obj = self.update(issue_obj, **update_info)
            self.session.refresh(issue_obj)
        return issue_obj

    def delete_issue(self, issue_id, auto_close=False):
        issue_obj = self.get_issue_detail(issue_id)

        with session_scope(self.session, auto_close=auto_close):
            self.delete(issue_obj)
