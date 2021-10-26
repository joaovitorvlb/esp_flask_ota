from app import db, migrate, create_app
from app.models.devices import Dispositivos, Firmware

from OpenSSL import SSL


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app, db=db, Dispositivos=Dispositivos, Firmware=Firmware, migrate=migrate
    )


@app.context_processor
def utility_processor():
    def format_mac(mac):
        return ":".join(mac[i : i + 2] for i in range(0, 12, 2))

    return dict(format_mac=format_mac)


if __name__ == "__main__":
    context = SSL.Context(SSL.SSLv23_METHOD)
    context.use_privatekey_file("server.key")
    context.use_certificate_file("server.crt")
    app.run(host="0.0.0.0", threaded=True)
