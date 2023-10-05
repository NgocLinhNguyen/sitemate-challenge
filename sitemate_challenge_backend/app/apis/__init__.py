import types
from flask import Flask
from app.common.errors import (
    BadRequestException, PermissionDeniedException, NotFoundException,
    UnprocessableEntityException, ConflictException
)
from flask_cors import CORS

db = types.SimpleNamespace()


def init_app(app_name=__name__):
    # Config App
    flask_app = Flask(app_name, instance_relative_config=True)
    flask_app.url_map.strict_slashes = False
    CORS(flask_app)

    # Config DB
    from app.databases.session import db_engine, db_flask_session
    engine = db_engine()
    db_flask_session.configure(bind=engine)
    db.session_factory = db_flask_session

    __config_blueprints(flask_app)
    __config_error_handlers(flask_app)
    return flask_app


def __config_blueprints(flask_app):
    from app.apis.issue_apis import issues_routes
    flask_app.register_blueprint(
        issues_routes, url_prefix='/api/v1/issues'
    )


def __config_error_handlers(flask_app):
    @flask_app.errorhandler(BadRequestException)
    def bad_request(error):
        return {'error': str(error) or 'Bad request'}, 400

    @flask_app.errorhandler(500)
    def server_error_page(error):
        return {'error': 'Internal server error'}, 500

    @flask_app.errorhandler(ConflictException)
    def conflict(error):
        return {'error': str(error) or 'Conflict'}, 409

    @flask_app.errorhandler(PermissionDeniedException)
    def permission_denied(error):
        return {'error': str(error) or 'Permission denied'}, 401

    @flask_app.errorhandler(NotFoundException)
    def not_found(error):
        return {'error': str(error) or 'Resource not found'}, 404

    @flask_app.errorhandler(UnprocessableEntityException)
    def unprocessable_entity(error):
        return {'error': str(error) or 'Unprocessable Entity'}, 422
