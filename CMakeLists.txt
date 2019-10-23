cmake_minimum_required(VERSION 3.15)
project(python_embed)

set(CMAKE_CXX_STANDARD 14)

find_package (Python3 COMPONENTS Interpreter Development)

include_directories(${Python3_INCLUDE_DIRS})
link_libraries(${Python3_LIBRARIES})
add_executable(python_embed main.cpp)
