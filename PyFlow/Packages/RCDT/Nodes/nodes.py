from RCDT.Nodes.core import PyflowNode, RosNode

from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped

from rcdt_utilities_msgs.action import Moveit
from rcdt_utilities_msgs.srv import AddMarker


class RvizMark:
    def __init__(self, ui: RosNode):
        self.ui = ui
        ui.ros_msg = PoseStamped()
        ui.client = PyflowNode.node.create_client(
            AddMarker, "/rviz_controller/add_marker"
        )
        ui.run_async = self.run_async

    def run_async(self) -> None:
        request = AddMarker.Request()
        request.marker_pose = self.ui.get_message()
        self.ui.call_service(request)


class MoveitMove:
    def __init__(self, ui: RosNode):
        self.ui = ui
        ui.ros_msg = PoseStamped()
        ui.client = ActionClient(PyflowNode.node, Moveit, "/moveit_controller")
        ui.run_async = self.run_async

    def run_async(self) -> None:
        goal = Moveit.Goal()
        goal.goal_pose = self.ui.get_message()
        goal.goal_pose.header.frame_id = "fr3_link0"
        self.ui.call_action(goal)
