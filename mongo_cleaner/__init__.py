class Cleaner(object):
    """Stale data cleaner for MongoDB."""

    def __init__(self, structure, db):
        self.db = db
        self.structure = structure

    def clean(self, dry_run=False):
        for collection, rules in self.structure.items():
            print 'searching', collection
            for doc in self.db[collection].find():
                for field, destination in rules:
                    foreign_id = doc.get(field)
                    if not foreign_id or not self.db[destination].find_one(doc[field]):
                        print 'removing', doc
                        if not dry_run:
                            self.db[collection].remove(doc)
            print 'cleaned', collection
