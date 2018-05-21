from flask import Flask
from flask_graphql import GraphQLView
from schema.restaurants_schema import restaurants_schema
from schema.user_schema import users_schema
from database import db_session, Base, engine, init_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.debug = True

app.add_url_rule(
    '/graphql/users',
    view_func=GraphQLView.as_view(
        'graphql_user',
        schema=users_schema,
        graphiql=True  # for having the GraphiQL interface
    )
)

app.add_url_rule(
    '/graphql/restaurants',
    view_func=GraphQLView.as_view(
        'graphql_restaurant',
        schema=restaurants_schema,
        graphiql=True  # for having the GraphiQL interface
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    return "Go to /graphql"


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0')
