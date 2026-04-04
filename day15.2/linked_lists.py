class Song:
    def __init__(self, title, next=None):
        self.title = title
        self.next = next

class Playlist:
    def __init__(self):
        self.head = None
    
    def add_to_end(self, title):
        new_song = Song(title)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_song
            return
        self.head = new_song

    def add_to_start(self, title):
        new_song = Song(title)
        new_song.next = self.head
        self.head = new_song

    def remove_song(self, title):
        current = self.head
        previous = None
        while current is not None:
            if current.title == title:
                if previous is None:
                    self.head = current.next
                    return
                else:
                    previous.next = current.next
                    return
            previous = current
            current = current.next
        return None           

    def show_playlist(self):
        current = self.head
        while current is not None:
            print(f"Song title: {current.title}")
            current = current.next

    def now_playing(self):
        if self.head is not None:
            return self.head.title
        return None

    def skip(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next

    def song_count(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

def demo():
    playlist = Playlist()
    playlist.add_to_start("Love")
    playlist.add_to_end("Mystery")
    playlist.add_to_start("Trance")
    playlist.add_to_end("What is Love?")
    playlist.add_to_start("Serene Calm")
    playlist.show_playlist()
    playlist.skip()
    playlist.skip()
    playlist.remove_song("Mystery")
    print("\n")
    playlist.show_playlist()
    
demo()
    