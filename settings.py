import os
from domain import DOMAIN

# mongo connection string 
# see https://docs.mongodb.com/manual/reference/connection-string/
MONGO_URI = os.environ.get('MONGO_URI')

# methods allowed at the resource (collection) endpoint
# POST = add new document(s)
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# methods allowed at the item (document) endpoint
# PATCH = edit a document
# PUT = replace a document
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# CORS support
# Allow access from all domains (javascript/web clients)
# see https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
X_DOMAINS = '*'