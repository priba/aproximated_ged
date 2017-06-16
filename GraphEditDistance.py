class GraphEditDistance(object):
    """
        An abstract class representing the Graph edit distance.
    """

    def __init__(self):
        pass

    def __substitution(self):
        raise NotImplementedError

    def __insertion(self):
        raise NotImplementedError

    def __deletion(self):
        raise NotImplementedError

    def ged(self, g1, g2):
        raise NotImplementedError