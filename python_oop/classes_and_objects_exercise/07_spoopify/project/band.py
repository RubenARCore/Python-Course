from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: list = []

    def add_album(self, album: Album):
        if album.name in [a.name for a in self.albums]:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self,album_name: str):
        if album_name not in [a.name for a in self.albums]:
            return f"Album {album_name} is not found."
        elif album_name in [a.name for a in self.albums if a.published == True]:
            return f"Album has been published. It cannot be removed."
        else:
            for album in self.albums:
                if album.name == album_name:
                    self.albums.remove(album)
                    return f"Album {album_name} has been removed."
            return None

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f"{album.details()}\n"
        return result