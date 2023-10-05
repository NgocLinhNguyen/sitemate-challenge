import os
from dotenv import load_dotenv
load_dotenv()

from app.apis import init_app, db  # noqa

flask_app = init_app()


@flask_app.teardown_appcontext
def shutdown_session(response_or_exc):
    db.session_factory.remove()
    return response_or_exc


if __name__ == '__main__':
    from alembic.config import Config
    from alembic import command

    migrations_dir = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(migrations_dir, 'alembic.ini')
    config = Config(config_file)
    command.upgrade(config, 'head')

    flask_app.run(debug=True, host='0.0.0.0', port='8000')
