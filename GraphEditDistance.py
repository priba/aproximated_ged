class GraphEditDistance:
    """
        An abstract class representing the Graph edit distance.
    """

    def __substitution__(self):
        raise NotImplementedError

    def __insertion__(self):
        raise NotImplementedError

    def __deletion__(self):
        raise NotImplementedError
