"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    playlists_songs = db.relationship('PlaylistSong', backref='playlist')
    songs = db.relationship('Song', secondary='playlist_songs', backref='playlist')

    def __repr__(self):
        pl = self
        return f"<PlayList id={pl.id} name={pl.name} description={pl.description} >"



class Song(db.Model):
    """Song."""
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=False)

    playlists_songs = db.relationship('PlaylistSong', backref='song')
    playlists = db.relationship('Playlist', secondary='playlist_songs', backref='song')

    def __repr__(self):
        s = self
        return f"<Song id={s.id} title={s.title} artist={s.artist} >"



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "playlist_songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

  


    def __repr__(self):
        pls = self
        return f"<Playlist_Song id={pls.id} playlist_id={pls.playlist_id} song_id={pls.song_id} >"




# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
