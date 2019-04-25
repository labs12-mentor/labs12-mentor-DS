"""
Data science Flask API endpoint
"""

from flask import Flask, jsonify
import os
import psycopg2 as pg


# database connection parameters
PORT = os.environ.get('PORT')
URL = os.environ.get('URL')
USER = os.environ.get('USER')
PASS = os.environ.get('PASS')
DBNAME = os.environ.get('DBNAME')

# TODO - initiate connection using psycopg2


# EB looks for an 'application' callable by default.
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Test route"""
    return 'Hello world'


@app.route('/matches/<org_id>')
def organization_matches(org_id=1):
    """
    Returns JSON object of mentor-mentee matches for a given organization

    Parameters
    ----------
    org_id : str
        Unique identifier of the organization for which to make matches

    Returns
    -------
    success : json

    """
    try:
        pass
        # TODO : get mentees in need of match

        # TODO : for each mentee get mentors that would be possible matches (top 5)

        # TODO : write matches into match table

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
