class Piece(object):
    """
    Points contain zero or more Pieces.
    """

    @property
    def color(self):
        'The side this Piece belongs to.'
        return self._color

    @property
    def num(self):
        'The number of this Piece in range [0..14]'
        return self._num

    def __init__(self, color, num):
        assert num >= 0 and num <= 15, \
            "number out of range [0,15]: {}".format(num)
        assert color in (WHITE, BLACK), \
            "color must be '{}' or '{}': {}".format(WHITE, BLACK, color)
        self._color = color
        self._num = num

    def __repr__(self):
        return "{}:{}".format(self.color, self.num)

    def __hash__(self):
        return (100 if self.color == WHITE else 200) + self.num

    def copy(self):
        """
        Return a deep copy of this Piece.
        """
        return Piece(self.color, self.num)