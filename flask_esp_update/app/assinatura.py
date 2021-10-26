from app.rotas.devices import bp_device


def init_app(app):
    app.register_blueprint(bp_device)
