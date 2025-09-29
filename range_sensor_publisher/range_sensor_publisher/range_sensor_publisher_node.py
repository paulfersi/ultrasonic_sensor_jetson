import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import smbus
import time

I2C_ADDR = 0x08
bus = smbus.SMBus(0)

class RangeSensorPublisherNode(Node):

    def __init__(self):
        super().__init__('range_sensor_publisher_node')
        self.publisher_ = self.create_publisher(Float64, 'range_sensor_distance_cm',10)
        timer_period = 0.3
        self.timer = self.create_timer(timer_period,self.timer_callback)
        self.distance = Float64()

    def timer_callback(self):
        msg = Float64()
        self.distance = self.read_distance
        if self.distance is not None:
            msg.data = self.distance
            self.publisher_.publish(msg)
            self.get_logger().info(f'Publishing :{msg.data}')
        else:
            self.get_logger().info(f'I2C error')
        
    
    def read_distance(self):
        try:
            data = bus.read_i2c_block_data(I2C_ADDR, 0, 2)
            distance_mm = (data[0] << 8) | data[1]
            distance_cm = distance_mm /10.0
            return distance_cm
        except Exception as e:
            print("I2C Error: ", e)
            return None


    def main(args=None):
        rclpy.init(args=args)
        node = RangeSensorPublisherNode()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()


    if __name__ == '__main__':
        main()

    
