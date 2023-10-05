from app.apis import db
from flask import request
from app.databases.services.issue import IssueService
from flask import Blueprint

issues_routes = Blueprint('issues_routes', __name__)


def init_service():
    session = db.session_factory()
    return IssueService(session)


@issues_routes.route('/', methods=('GET', 'POST'))
def issues():
    methods_mapping = {
        'GET': index,
        'POST': create
    }
    return methods_mapping.get(request.method)()


@issues_routes.route('/<issue_id>', methods=('GET', 'PATCH', 'DELETE'))
def issue(issue_id):
    methods_mapping = {
        'GET': get,
        'PATCH': update,
        'DELETE': delete
    }
    return methods_mapping.get(request.method)(issue_id)


def index():
    issue_service = init_service()
    issue_objs = issue_service.list_issues(limit=None, offset=None)
    response = [issue_obj.to_dict() for issue_obj in issue_objs]
    print(response)
    return {
        'data': {
            'issues': response
        }
    }, 200


def create():
    data = request.get_json()
    issue_service = init_service()
    new_issue = issue_service.create_issue(
        title=data.get('title'),
        description=data.get('description')
    )
    response = new_issue.to_dict()
    print(response)
    return {
        'data': {
            'issue': response
        }
    }, 201


def get(issue_id):
    issue_service = init_service()
    response = issue_service.get_issue_detail(issue_id).to_dict()
    print(response)
    return {
        'data': {
            'issue': response
        }
    }, 200


def update(issue_id):
    data = request.get_json()
    issue_service = init_service()
    issue_updated = issue_service.update_issue(
        issue_id=issue_id,
        title=data.get('title'),
        description=data.get('description')
    )
    response = issue_updated.to_dict()
    print(response)
    return {
        'data': {
            'issue': response
        }
    }, 204


def delete(issue_id):
    issue_service = init_service()
    issue_service.delete_issue(issue_id)
    return {}, 204
