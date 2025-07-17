import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import subprocess

class KeypressListener(Node):
    def __init__(self):
        super().__init__('keypress_listener')
        self.subscription = self.create_subscription(
            String,
            '/keypress',
            self.keypress_callback,
            10)
        self.target_key = 'n'  # Change this to whatever key string you expect

    def keypress_callback(self, msg):
        key = msg.data.lower()
        self.get_logger().info(f"Key pressed: {key}")

        if key == self.target_key:
            self.get_logger().info(f"Target key '{self.target_key}' detected! Running subprocess...")
            # Replace with your command or script path
            subprocess.Popen(['python3', 'sound.py'])

def main(args=None):
    rclpy.init(args=args)
    node = KeypressListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
