from AbstractGraph import *
from AGraphPySide.Settings import *
from AGraphPySide import BaseNode


class StringToInt(BaseNode.Node, AGNode):
    def __init__(self, name, graph):
        super(StringToInt, self).__init__(name, graph, spacings=Spacings)
        self.in_str = self.add_input_port('str', AGPortDataTypes.tString)
        self.out_int = self.add_output_port('int', AGPortDataTypes.tInt)
        portAffects(self.in_str, self.out_int)

    @staticmethod
    def get_category():
        return 'Convert'

    def compute(self):

        str_data = self.in_str.get_data()
        try:
            self.out_int.set_data(int(str_data), False)
        except Exception, e:
            print e
