import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Adjust if using a different type
import os
from playsound import playsound  # Optional: your "do something"
import sys
print(f"Python: {sys.executable}")

class KeyPressListener(Node):
    

    def __init__(self):
        super().__init__('key_press_listener')
        self.subscription = self.create_subscription(
            String,                   # Message type
            '/keyboard/keypress',         # Topic name
            self.listener_callback,   # Callback function
            10                        # QoS
        )
        print(f"Python: {sys.executable}")

    def listener_callback(self, msg):
        key = msg.data.strip().lower()  # Normalize input
        self.get_logger().info(f"Received key press: {key}")
        if key == 'n':
            self.handle_n_press()

    def handle_n_press(self):
        script_path = os.path.abspath(__file__)
        self.get_logger().info("Key 'n' was pressed! Doing something...")
        # Do your action here (e.g., play sound)
        # sound_path = '/absolute/path/to/beep.wav'
        #playsound(script_path + '/../sounds/yeetSound.mp3')

def main(args=None):
    rclpy.init(args=args)
    node = KeyPressListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
