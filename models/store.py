from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')  # what items the store has

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod        #remain to be classmethod because it needs to return object
    def find_by_name(cls, name):    #return ItemModel object
        return cls.query.filter_by(name=name).first() #does not requre any connection setup

    def save_to_db(self):
        db.session.add(self)    #session is bunch of objects
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
