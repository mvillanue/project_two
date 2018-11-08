from bokeh.core.tests.test_has_props import Parent
class NodeT:
    def __init__(self,parent,children,values,gini,nElements, _class):
        self.parent=parent
        self.children = children
        self.values
        self.gini = 0
        self.nElements = nElements
        self._class = _class