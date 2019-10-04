class FileInfo:

    def __init__(self, path, coord):
        self.path = path
        self.ext = path.split('.')[-1]
        self.coord = coord
