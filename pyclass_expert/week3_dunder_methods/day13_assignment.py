# Day 13 Assignment: Container & Sequence Protocols
# ----------------------------------------------------------------------
# Instructions: Complete the Playlist class to support indexing, slicing,
# lengths, deletion, and case-insensitive membership checks.
# Run 'python day13_test.py' to verify your solutions.

class Playlist:
    """
    Requirements:
    1. Constructor accepts 'name' (str) and initializes internal list '_songs' to empty list.
    2. Implement '__len__(self)' to return the total number of songs.
    3. Implement '__getitem__(self, index)' to return song at index (supports slicing too).
    4. Implement '__setitem__(self, index, value)' to replace song at index:
       - Validate: if 'value' is not a string, raise TypeError("Song must be a string").
       - Otherwise, update internal list at 'index'.
    5. Implement '__delitem__(self, index)' to delete song at 'index'.
    6. Implement '__contains__(self, song)' to perform case-insensitive membership checks:
       - Returns True if 'song' (case-insensitive) matches any song in the playlist.
       - Example: If playlist contains ["Yellow Submarine"], then "yellow submarine" in playlist is True.
    """
    def __init__(self, name):
        # TODO: Initialize name and empty songs list
        pass

    def __len__(self):
        # TODO: Return length of songs list
        pass

    def __getitem__(self, index):
        # TODO: Return song or slice of songs
        pass

    def __setitem__(self, index, value):
        # TODO: Validate type and assign
        pass

    def __delitem__(self, index):
        # TODO: Delete from list
        pass

    def __contains__(self, song):
        # TODO: Perform case-insensitive containment check
        pass
