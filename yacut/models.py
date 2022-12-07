from datetime import datetime

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256),index=True, nullable=False)
    short = db.Column(db.String(16), index=True, unique=True,
                      nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


    def to_dict(self):
       return dict(
            id = self.id,
            original = self.original,
            short = self.short,
            timestamp = self.timestamp,
        )

    def from_dict(self, data):
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])
