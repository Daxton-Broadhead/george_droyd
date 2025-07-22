import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Adjust if using a different type
from std_msgs.msg import Int32
import os

import sys
import simpleaudio as sa

print("Current working directory:", os.getcwd())





class KeyPressListener(Node):
    

    def __init__(self):
        super().__init__('key_press_listener')
        self.subscription = self.create_subscription(
            Int32,                   # Message type
            '/keyboard/keypress',         # Topic name
            self.listener_callback,   # Callback function
            10                        # QoS
        )
        print(f"Python: {sys.executable}")

    def listener_callback(self, msg):
        key = msg.data  # Normalize input
        print(key)
        self.get_logger().info(f"Received key press: {key}")
        if key == 78:
            self.handle_n_press()

    def handle_n_press(self):
        print('stuff is being done')
        script_path = os.path.abspath(__file__)
        self.get_logger().info("Key 'n' was pressed! Doing something...")
        # Do your action here (e.g., play sound)
        wave_obj = sa.WaveObject.from_wave_file("src/key_press/sounds/yeetSound.wav")
        wave_obj.play()
        # play_obj = wave_obj.play()
        # play_obj.wait_done()  # Wait until sound has finished playing


def main(args=None):
    rclpy.init(args=args)
    node = KeyPressListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
