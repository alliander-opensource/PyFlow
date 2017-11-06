from AbstractGraph import *
from AGraphPySide.Settings import *
from AGraphPySide import BaseNode


class StringUpper(BaseNode.Node, AGNode):
    def __init__(self, name, graph):
        super(StringUpper, self).__init__(name, graph, spacings=Spacings)
        self.in_str = self.add_input_port('str', AGPortDataTypes.tString)
        self.out_str = self.add_output_port('upper str', AGPortDataTypes.tString)
        portAffects(self.in_str, self.out_str)

    @staticmethod
    def get_category():
        return 'String'

    def compute(self):

        str_data = self.in_str.get_data()
        try:
            self.out_str.set_data(str_data.upper(), False)
        except Exception, e:
            print e
