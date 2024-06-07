from flask import Flask, jsonify, request
import graphene
from graphene import ObjectType, String, Int, List, Field

app = Flask(__name__)



if __name__ == '__main__':
    app.run()