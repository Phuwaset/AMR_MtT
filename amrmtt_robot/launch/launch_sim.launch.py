import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    package_name = 'amrmtt_robot'

    # 📍 Path ของ world.sdf ใน package
    world_path = os.path.join(
        get_package_share_directory(package_name),
        'gazebo_gz_ros',
        'world.sdf'
    )

    # 🟢 Include Robot State Publisher
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory(package_name),
                'launch',
                'rsp.launch.py'
            )
        ),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # 🟡 เปิด world ของเราใน Gazebo Fortress
    gazebo = ExecuteProcess(
        cmd=['ign', 'gazebo', world_path],
        output='screen'
    )

    # 🔵 Spawn robot จาก robot_description หลังจาก world พร้อม
    spawn_entity = TimerAction(
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

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity
    ])
