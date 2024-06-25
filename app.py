from flask import Flask, jsonify, request
import graphene
from graphql_server.flask import GraphQLView

app = Flask(__name__)

books = [
    {
        "id": "1",
        "name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "status": "read"
    },
    {
        "id": "2",
        "name": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "status": "unread"
    },
    {
        "id": "3",
        "name": "1984",
        "author": "George Orwell",
        "status": "in progress"
    }
]

class Book(graphene.ObjectType):
    id = graphene.String(description = " number of the book", required = True)
    name = graphene.String(description="Name of the book", required=True)
    author = graphene.String(description="Author of the book", required=True)
    status = graphene.String(description="Status of the book", required=True)

class Query(graphene.ObjectType):
    all_books = graphene.List(Book)

    def resolve_all_books(self, info):
        return books
    
class Query(graphene.ObjectType):
    all_books = graphene.List(Book)

    def resolve_all_books(self, info):
        return books


class Mutation(graphene.ObjectType):
    add_book = graphene.Field(Book,
                              name = graphene.String(required=True),
                              author = graphene.String(required=True),
                              status = graphene.String(required=True)
                              )

    def resolve_add_book(self, info, name, author, status):
        new_id = len(books) + 1
        new_book = Book(id = new_id, name = name, author = author, status = status)
        books.append(new_book)
        return new_book


schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True
))

@app.route('/', methods=['POST'])
def graphql_endpoint():
    data = request.get_json()
    result = schema.execute(data.get('query'))
    return jsonify(result.data)

if __name__ == '__main__':
    app.run()