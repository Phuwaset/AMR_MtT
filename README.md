## AMRMTT Robot (ROS2 Humble)

Project kmutnb(mtt13) **Autonomous Mobile Robot (AMR)**  
use and develop with ROS2 (Humble) simulation, joints  
**URDF/XACRO**, **RViz2**, and **Gazebo simulation**

---

## 🗂️ Stature of Workspace

```bash
~/amr_MtT/
├── build/                 # build files (colcon สร้างให้)
├── install/               # install files (colcon สร้างให้)
├── log/                   # log จากการรัน
└── src/
    └── amrmtt_robot/
        ├── CMakeLists.txt
        ├── package.xml
        ├── description/
        │   ├── robot_core.xacro
        │   ├── inertial_macros.xacro
        │   └── robot_urdf.xacro
        ├── meshes/
        │   ├── Chassis_link.STL
        │   ├── Left_Wheel_Link.STL
        │   ├── Right_Wheel_Link.STL
        │   ├── L_B_Caster_W_Link.STL
        │   ├── L_F_Caster_W_Link.STL
        │   ├── R_B_Caster_W_Link.STL
        │   └── R_F_Caster_W_Link.STL
        ├── launch/
        │   ├── rsp.launch.py
        │   └── display.launch.py
        └── rviz/
            └── view_robot.rviz
```

---

## Create your workspace 

```bash
mkdir -p ~/amr_MtT/src
cd ~/amr_MtT/src
```

## Create new package
```bash
ros2 pkg create --build-type ament_cmake amrmtt_robot
```

## update CMakeLists.txt
```bash
cmake_minimum_required(VERSION 3.5)
project(amrmtt_robot)

find_package(ament_cmake REQUIRED)

// **************** Focus  launch meshes rviz description ******************* //
install(DIRECTORY
  launch
  meshes
  rviz
  description
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
```


## update package.xml
```bash
<?xml version="1.0"?>
<package format="3">
  <name>amrmtt_robot</name>
  <version>0.0.1</version>
  <description>Robot description and visualization package for AMR MTT project.</description>

  <maintainer email="your_email@example.com">Phuwaset Sibta</maintainer>
  <license>MIT</license>

  <buildtool_depend>ament_cmake</buildtool_depend>

  <exec_depend>joint_state_publisher</exec_depend>
  <exec_depend>joint_state_publisher_gui</exec_depend>
  <exec_depend>robot_state_publisher</exec_depend>
  <exec_depend>rviz2</exec_depend>
  <exec_depend>xacro</exec_depend>

</package>
```


## State == gazebo lauch sim
```bash
ros2 launch amrmtt_robot launch_sim.launch.py world:=my_world.sdf
```
## http://gazebosim.org/docs/fortress/getstarted/ Docs / Gazebo Fortress 


```bash
gz sim shapes.sdf  # Fortress uses "ign gazebo" instead of "gz sim"

gz sim shapes.sdf -v 4  # Fortress uses "ign gazebo" instead of "gz sim"

gz sim -s shapes.sdf -v 4  # Fortress uses "ign gazebo" instead of "gz sim"

```

## Problem if you command gazebo on your terminal but the UI is not available.
ตรวจสอบว่ามี gazebo อยู่ในเครื่องหรือไม่
```bash
which gazebo
```

รันแบบ verbose เพื่อดู log
```bash
gazebo --verbose
```

แต่สาเหตุที่มัน “ไม่ขึ้น GUI” และค้างแบบนี้ เป็นเพราะ
```bash
[Err] [Master.cc:96] EXCEPTION: Unable to start server[bind: Address already in use].
There is probably another Gazebo process running.
```

check process
```bash
ps aux | grep gazebo
```
