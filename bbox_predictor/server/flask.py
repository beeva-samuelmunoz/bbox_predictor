"""Web views for the server
"""

from flask import render_template, send_from_directory


def init_flask(app):


    @app.route('/')
    def main():
        return render_template('predictor.html')


    @app.route('/static/<path:filename>')
    def send_static(filename):
        return send_from_directory("templates", filename)
