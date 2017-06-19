class GraphEditDistance(object):
    """
        An abstract class representing the Graph edit distance.
    """

    # NODE
    def node_substitution(self, g1, g2):
        raise NotImplementedError

    def node_insertion(self, g):
        raise NotImplementedError

    def node_deletion(self, g):
        raise NotImplementedError

    # EDGE
    def edge_substitution(self, g1, g2):
        raise NotImplementedError

    def edge_insertion(self, g):
        raise NotImplementedError

    def edge_deletion(self, g):
        raise NotImplementedError

    # Graph Edit Distance
    def ged(self, g1, g2):
        raise NotImplementedError
