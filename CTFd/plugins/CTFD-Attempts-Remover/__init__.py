import os

from flask import send_from_directory

from CTFd.models import db
from CTFd.plugins import register_plugin_script

from .models import (  # noqa: F401 — registers the tables with SQLAlchemy
    ExcludedChallenge,
    SingleAttemptLog,
    SingleAttemptRequest,
    UnblockLog,
    UnblockRequest,
)
from .routes import api_bp, remover_bp


def load(app):
    plugin_root = os.path.dirname(__file__)
    assets_root = os.path.join(plugin_root, "assets")

    with app.app_context():
        db.create_all()

    app.register_blueprint(remover_bp)
    app.register_blueprint(api_bp)

    @app.route("/plugins/ctfd-attempts-remover/assets/<path:path>")
    def attempts_remover_assets(path):
        return send_from_directory(assets_root, path)

    register_plugin_script("/plugins/ctfd-attempts-remover/assets/remover_i18n.js")
    register_plugin_script("/plugins/ctfd-attempts-remover/assets/settingsremover.js")
