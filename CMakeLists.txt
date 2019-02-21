cmake_minimum_required(VERSION 2.8)

project(sys_wait_h)

add_executable(example example.c sys/wait.h)

target_include_directories(example PRIVATE ${CMAKE_SOURCE_DIR})
