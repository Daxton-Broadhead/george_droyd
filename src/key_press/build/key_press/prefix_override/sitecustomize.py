import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/daxton/simulation/ros2_ws/src/key_press/install/key_press'
