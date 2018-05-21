from flask import Flask
from flask_graphql import GraphQLView
from schema.restaurants_schema import restaurants_schema
from database import db_session, Base, engine
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.debug = True

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


@app.route('/create-tables')
def create_table():
    Base.metadata.create_all(bind=engine)
    return 'Database tables created, hopefully'


@app.route('/drop-tables')
def drop_table():
    Base.metadata.drop_all(bind=engine)
    return 'Database tables dropped, hopefully'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
