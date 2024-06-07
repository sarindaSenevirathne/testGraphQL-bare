from flask import Flask, jsonify, request
import graphene
import os

app = Flask(__name__)

# Sample data
books = [
    {
        "author": "me",
        "id": 1,
        "name": "adam sandler",
        "status": "read"
    }
]

class Book(graphene.ObjectType):
    id = graphene.String(description="ID of the book", required=True)
    name = graphene.String(description="Name of the book", required=True)
    author = graphene.String(description="Author of the book", required=True)
    status = graphene.String(description="Status of the book", required=True)

class Query(graphene.ObjectType):
    all_books = graphene.List(Book)

    def resolve_all_books(self, info):
        return books

schema = graphene.Schema(query=Query)

@app.route('/graphql', methods=['POST'])
def graphql_endpoint():
    data = request.get_json()
    result = schema.execute(data.get('query'))
    if result.errors:
        return jsonify({'errors': [str(e) for e in result.errors]})
    return jsonify(result.data)

if __name__ == '__main__':
    app.run()