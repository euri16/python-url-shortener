from urlshortener.core import db
from sqlalchemy import UniqueConstraint, Index, and_
from urlshortener.lib.IntEncoder import IntEncoder


class ShortenedUrl(db.Model):
    """
        Stores the urls that had been shortened
    """
    __tablename__ = "shortened_urls"
    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)
    long_url = db.Column(db.String(499), nullable=False)
    openings = db.Column(db.Numeric, nullable=False, default=0)

    __table_args__ = (Index("id_idx", "id"),
                      Index("url_idx", "long_url"),
                      Index("openings_idx", "openings"))

    def __init__(self, long_url):
        self.long_url = long_url
        self.openings = 0

    def __repr__(self):  # pragma no cover
        return "<ShortenedUrl(id={0}, long_url={1}, openings={2}>".format(
            self.id, self.long_url, self.openings)

    def to_serializable(self):
        return {
            "id": self.id,
            "long_url": self.long_url,
            "openings": self.openings
        }

    def encoded_id(self):
        return IntEncoder().encode(self.id)
