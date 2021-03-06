import os
import flask

def inject_static_url():
    """Adds `STATIC_URL` variable to template context.
    """
    app = flask.current_app
    static_url = os.environ.get('STATIC_URL', app.static_url_path)
    if not static_url.endswith('/'):
        static_url += '/'
    return dict(
        static_url=static_url
    )