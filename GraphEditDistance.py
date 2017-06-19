class GraphEditDistance(object):
    """
        An abstract class representing the Graph edit distance.
    """

    def substitution(self, values1, values2):
        raise NotImplementedError

    def insertion(self, values):
        raise NotImplementedError

    def deletion(self, values):
        raise NotImplementedError

    def ged(self, g1, g2):
        raise NotImplementedError
