"""
Data science Flask API endpoint
"""

from flask import Flask, jsonify
import os
import psycopg2 as pg


# database connection parameters
PORT = int(os.environ.get('PORT'))
URL = os.environ.get('URL')
USER = os.environ.get('USER')
PASS = os.environ.get('PASS')
DBNAME = os.environ.get('DBNAME')
TIMEOUT = 5


# EB looks for an 'application' callable by default.
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Test route"""
    return 'Hello world'


@app.route('/testconnection')
def test_connection():
    """
    Tests connection to backend database
    """
    try:
        conn = pg.connect(host=URL,
                          port=PORT,
                          dbname=DBNAME,
                          user=USER,
                          password=PASS,
                          connect_timeout=TIMEOUT)
        conn.close()
        return 'Connection Successful!'
    except BaseException as e:
        return 'An exception occurred when connecting: {}'.format(e)


@app.route('/matches/<org_id>')
def organization_matches(org_id=1):
    """
    Writes new matches into table for a given organization

    Parameters
    ----------
    org_id : str
        Unique identifier of the organization for which to make matches

    Returns
    -------
    success : json

    """
    try:
        # connect to database
        conn = pg.connect(host=URL,
                          port=PORT,
                          dbname=DBNAME,
                          user=USER,
                          password=PASS,
                          connect_timeout=TIMEOUT)
        cursor = conn.cursor()

        # TODO : get mentees in need of match

        # TODO : for each mentee get mentors that would be possible matches (top 5)

        # TODO : write matches into match table

        # TODO : commit transaction

        cursor.close()
        conn.close()

    except:
        # TODO: handle exceptions
        return jsonify({'success': False,
                        'org_id' : org_id})

    return jsonify({'success' : True,
                    'org_id' : org_id})


# run the app!
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run(host='0.0.0.0')
