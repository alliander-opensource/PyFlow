from AbstractGraph import *
from AGraphPySide.Settings import *
from AGraphPySide import BaseNode


class Len(BaseNode.Node, AGNode):
    def __init__(self, name, graph):
        super(Len, self).__init__(name, graph, spacings=Spacings)
        self.in_arr = self.add_input_port('iterable', AGPortDataTypes.tAny)
        self.out_len = self.add_output_port('len', AGPortDataTypes.tFloat)
        self.out_result = self.add_output_port('result', AGPortDataTypes.tBool)
        portAffects(self.in_arr, self.out_result)
        portAffects(self.in_arr, self.out_len)

    @staticmethod
    def get_category():
        return 'Array'

    def compute(self):

        in_arr = self.in_arr.get_data()
        try:
            self.out_len.set_data(len(in_arr), False)
            self.out_result.set_data(True, False)
        except Exception, e:
            self.out_result.set_data(False, False)
            print e
