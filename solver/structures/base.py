from functools import reduce
from typing import Any, Dict, Hashable
from graph import Graph


class Structure:
    """
    Base class for all kinds of road structures.
    """

    def __init__(self, g: Graph, node_labels: Dict[str, Hashable]) -> None:
        """
        For passing all relavant internal 
        nodes to this structure
        """
        self.graph = g
        self.internal_nodes = node_labels

    def __call__(self, *args: Any, **kwds: Any) -> None:
        """
        For adding or deleting edges
        between the internal nodes.
        """
        pass


class Octagonal_cell(Structure):
    def __init__(self, g: Graph, node_labels: Dict[str, Hashable]) -> None:
        assert reduce(lambda x, y: x and y, [x in self.internal_nodes.keys() for x in [
            "N", "E", "W", "S", "NE", "SW", "SE", "NW"]]) and (len(node_labels) == 8)
        super().__init__(g, node_labels)

    def __call__(self, active_dir: Dict[str, bool], *args: Any, **kwds: Any) -> None:
        assert reduce(lambda x, y: x and y, [x in self.internal_nodes.keys() for x in [
            "N", "E", "W", "S", "NE", "SW", "SE", "NW"]]) and (len(active_dir) == 8)
        return super().__call__(*args, **kwds)


class Diamond_cell(Structure):
    def __init__(self, g: Graph, node_labels: Dict[str, Hashable]) -> None:
        assert reduce(lambda x, y: x and y, [x in self.internal_nodes.keys() for x in [
            "NE", "SW", "SE", "NW"]]) and (len(node_labels) == 4)
        super().__init__(g, node_labels)

    def __call__(self, active_dir: Dict[str, bool], *args: Any, **kwds: Any) -> None:
        assert reduce(lambda x, y: x and y, [x in self.internal_nodes.keys() for x in [
            "NE", "SW", "SE", "NW"]]) and (len(active_dir) == 4)
        return super().__call__(*args, **kwds)
