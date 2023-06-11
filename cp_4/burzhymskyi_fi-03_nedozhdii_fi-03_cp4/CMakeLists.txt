cmake_minimum_required(VERSION 3.24)
project(burzhymskyi_fi-03_nedozhdii_fi-03_cp4)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_C_COMPILER /opt/homebrew/opt/llvm/bin/clang)
set(CMAKE_CXX_COMPILER /opt/homebrew/opt/llvm/bin/clang++)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")

add_executable(burzhymskyi_fi-03_nedozhdii_fi-03_cp4 main.cpp)

target_link_libraries(burzhymskyi_fi-03_nedozhdii_fi-03_cp4 omp)