from __future__ import division, print_function, absolute_import

# from flask import Flask

from app import app


if __name__ == '__main__':
    app.run(debug=True, port=5000)
#    app.run(host='0.0.0.0', port=5000)
