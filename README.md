# Mongo-Cleaner

Suppose you have two collections: `users` and `pajamas`

users collection contains the following document:
    
    {'_id': 'foo@bar.com'}

`pajamas` collection contains the following document:

    {'_id': ObjectID('5048a4302b0c301603b8e74c'), 
     'user': 'foo@bar.com', 
     'color': 'pink'}

Suppose you delete the user's document and forgot to delete his pajama. Now the pajama document is stale and takes up space on your database.

This tool finds and removes stale documents.

## To istall:

    pip install mongo-cleaner

## Sample usage:

    import pymongo
    from mongo_cleaner import Cleaner

    structure = {
        'pajamas': [
            ('user', ['users'])
        ],
    }

    connection = pymongo.Connection()
    db = connection['pajamaapp']

    cleaner = Cleaner(structure, db)
    cleaner.clean()

### Note:

To see which documents are stale without removing them, pass `'dry_run=True'` to `clean()`.
