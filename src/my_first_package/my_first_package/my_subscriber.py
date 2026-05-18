import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose

# 거북이 위치 토픽(/turtle1/pose)을 실시간 구독해서
# 좌표를 계속 출력하는 Subscriber Node
class TurtlesimSubscriber(Node):
    def __init__(self):
        super().__init__('turtlesim_subscriber')
        self.subscription = self.create_subscription( # 이제 특정 topic 데이터를 받겠다
            Pose,
            '/turtle1/pose',
            self.callback,
            10
        )
    
    def callback(self, msg):
        print("X", msg.x , "Y", msg.y)  # 거북이 현재 위치 실시간 출력


def main():
    rp.init()

    turtlesim_subscriber = TurtlesimSubscriber() # Subscriber Node 객체 생성.
    rp.spin(turtlesim_subscriber) # 토픽 데이터 계속 기다려라

    turtlesim_subscriber.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()