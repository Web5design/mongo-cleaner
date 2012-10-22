class Cleaner(object):
    """Stale data cleaner for MongoDB."""

    def __init__(self, structure, db):
        self.db = db
        self.structure = structure

    def clean(self, dry_run=False):
        for collection, rules in self.structure.items():
            print 'searching', collection

            for doc in self.db[collection].find():

                for field, target_collections in rules:
                    remove = False

                    foreign_id = doc.get(field)
                    if foreign_id:
                        found = False

                        for target_collection in target_collections:
                            target_doc = self.db[target_collection].find_one(doc[field])
                            if target_doc:
                                found = True
                                break
                                
                        if not found:
                            remove = True
                    else:
                        remove = True

                    if remove:
                        if dry_run:
                            print 'not removing', doc
                        else:
                            print 'removing', doc
                            self.db[collection].remove(doc)
            print 'cleaned', collection
