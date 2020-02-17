cmake_minimum_required(VERSION 2.8.3)
project(temizlik_robotu_servis_istemci_ornek)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

add_service_files(
    FILES 
    BilgiServisiOrnek.srv
)

 generate_messages(
   DEPENDENCIES
   std_msgs
 )


catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

foreach(dir launch srv scripts)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach()