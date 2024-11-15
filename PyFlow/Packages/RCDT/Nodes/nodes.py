from RCDT.Nodes.core import PyflowNode, RosNode

from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
from moveit_msgs.msg import CollisionObject

from rcdt_utilities_msgs.action import Moveit
from rcdt_utilities_msgs.srv import AddMarker, AddObject
from std_srvs.srv import Trigger


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


class MoveitAddObject:
    def __init__(self, ui: RosNode):
        self.ui = ui
        ui.ros_msg = CollisionObject()
        ui.client = PyflowNode.node.create_client(
            AddObject, "/moveit_controller/add_object"
        )
        ui.run_async = self.run_async

    def run_async(self) -> None:
        request = AddObject.Request()
        request.object = self.ui.get_message()
        print(request)
        self.ui.call_service(request)


class MoveitClearObjects:
    def __init__(self, ui: RosNode):
        self.ui = ui
        ui.client = PyflowNode.node.create_client(
            Trigger, "/moveit_controller/clear_objects"
        )
        ui.run_async = self.run_async

    def run_async(self) -> None:
        request = Trigger.Request()
        self.ui.call_service(request)
