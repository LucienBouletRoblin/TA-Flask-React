from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView

from database import db_session, init_db

app = Flask(__name__)
CORS(app)
app.debug = True
init_db()

from general_schema import schema

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql_user',
        schema=schema,
        graphiql=True
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    return "Go to /graphql"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
