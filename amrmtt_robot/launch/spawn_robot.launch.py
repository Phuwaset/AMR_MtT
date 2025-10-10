from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command, LaunchConfiguration
import os

def generate_launch_description():

    # 📦 Package & path ของไฟล์ Xacro
    pkg_name = 'amrmtt_robot'
    xacro_subpath = 'description/robot.urdf.xacro'
    xacro_path = os.path.join(get_package_share_directory(pkg_name), xacro_subpath)

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    # 🦴 robot_description จาก xacro
    robot_description_content = Command(['xacro ', xacro_path])
    robot_description = {'robot_description': robot_description_content}

    return LaunchDescription([

        # 🟡 1. เปิด world เริ่มต้นของ Gazebo
        ExecuteProcess(
            cmd=['ign', 'gazebo'],
            output='screen'
        ),

        # 🟢 2. Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[robot_description]
        ),

        # 🔵 3. Spawn Robot หลัง 5 วินาที
        TimerAction(
            period=5.0,
            actions=[
                ExecuteProcess(
                    cmd=[
                        'ros2', 'run', 'ros_gz_sim', 'create',
                        '-topic', 'robot_description',
                        '-name', 'amrmtt_robot',
                        '-z', '0.01'
                    ],
                    output='screen'
                )
            ]
        )
    ])
