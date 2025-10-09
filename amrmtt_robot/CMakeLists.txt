cmake_minimum_required(VERSION 3.8)
project(amrmtt_robot)

find_package(ament_cmake REQUIRED)

# ติดตั้งทุก directory ที่มีไฟล์สำคัญ
install(
  DIRECTORY launch urdf meshes rviz config
  DESTINATION share/${PROJECT_NAME}
)

# ติดตั้ง folder ทั้งหมดที่ใช้ใน package
install(
  DIRECTORY launch description meshes rviz config
  DESTINATION share/${PROJECT_NAME}
)
ament_package()
