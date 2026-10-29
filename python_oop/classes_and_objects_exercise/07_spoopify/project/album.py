from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.songs: list[Song] = list(songs)
        self.published: bool = False

    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song.name in [s.name for s in self.songs]:
            return f"Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        elif song_name not in [s.name for s in self.songs]:
            return f"Song is not in the album."
        else:
            for song in self.songs:
                if song.name == song_name:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
            return None

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        return result