from PyFlow.Core import PinBase
from RCDT.Nodes.core import RosMessage
from rosidl_runtime_py import convert
import json

from geometry_msgs.msg import PoseStamped


class PoseStampedMsg:
    def __init__(self, ui: RosMessage):
        ui.compute_callback = self.compute
        self.px_pin: PinBase = ui.createInputPin("px", "FloatPin")
        self.py_pin: PinBase = ui.createInputPin("py", "FloatPin")
        self.pz_pin: PinBase = ui.createInputPin("pz", "FloatPin")

        self.ow_pin: PinBase = ui.createInputPin("ow", "FloatPin")
        self.ox_pin: PinBase = ui.createInputPin("ox", "FloatPin")
        self.oy_pin: PinBase = ui.createInputPin("oy", "FloatPin")
        self.oz_pin: PinBase = ui.createInputPin("oz", "FloatPin")

        self.out: PinBase = ui.createOutputPin("PoseStamped", "StringPin", "{}")

    def compute(self) -> None:
        msg = PoseStamped()
        msg.pose.position.x = self.px_pin.getData()
        msg.pose.position.y = self.py_pin.getData()
        msg.pose.position.z = self.pz_pin.getData()
        msg.pose.orientation.w = self.ow_pin.getData()
        msg.pose.orientation.x = self.ox_pin.getData()
        msg.pose.orientation.y = self.oy_pin.getData()
        msg.pose.orientation.z = self.oz_pin.getData()

        msg_dict = convert.message_to_ordereddict(msg)
        msg_json = json.dumps(msg_dict)

        self.out.setData(msg_json)
