"""Connect to the Database"""
import sqlite3
from datetime import datetime

import click
from flask import current_app, g


def get_db():
    """
    Get a database connection for the current request.

    This function checks if a database connection already exists 
    in Flask's `g` object (which is unique per request). 
    If not, it creates a new SQLite connection using the path 
    defined in `current_app.config['DATABASE']`.

    - The connection is stored in `g.db` so that it can be reused 
      within the same request.
    - The `row_factory` is set to `sqlite3.Row` so that query 
      results behave like dictionaries, allowing access by column name.

    Returns:
        sqlite3.Connection: An open SQLite database connection.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    """
    Close the database connection for the current request, if one exists.

    This function checks if `g.db` has been set during the request. 
    If a connection exists, it is closed and removed from `g`.

    Args:
        e (Exception, optional): An optional error object passed 
        by Flask when handling application teardown. Defaults to None.

    Returns:
        None
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


"""Create the Tables"""
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

"Register with the Application"

def init_app(app):
    """app.teardown_appcontext() tells Flask to call that function when cleaning up after returning the response.
    app.cli.add_command() adds a new command that can be called with the flask command."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    
