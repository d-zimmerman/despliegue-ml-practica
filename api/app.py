# -*- coding: utf-8 -*-
import settings
from flask import Flask, render_template
from views import router
from middleware import print_error404


app = Flask(__name__)
app.register_blueprint(router)


@app.errorhandler(404)
def page_not_found(error):
    print_error404()
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=settings.API_DEBUG)
