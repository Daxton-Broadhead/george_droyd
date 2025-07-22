import cv2 as cv
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class ImageNode(Node):
    def __init__(self):
        super().__init__('computer_vision_node')
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/rgbd_camera/image',  # Replace with your topic
            self.image_callback,
            10
        )
        cv.namedWindow("Camera View", cv.WINDOW_NORMAL)

    
    def image_callback(self, msg):
        try:
            # Convert ROS Image to OpenCV Image
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # Show the image in a window
            cv.imshow("Camera View", cv_image)
            cv.waitKey(1)  # Needed to refresh the window
        except Exception as e:
            self.get_logger().error(f"Could not convert image: {e}")



def main(args=None):
    rclpy.init(args=args)
    node = ImageNode()
    rclpy.spin(node)
    cv.destroyAllWindows()
    rclpy.shutdown()