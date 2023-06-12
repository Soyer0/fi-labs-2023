cmake_minimum_required(VERSION 3.8)

#Alias
set(This Bondar_Kistaiev_CP4)

#Set language
project(${This} LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)

set(Headers 
    LFSR.hpp
    Geffe.hpp
)

set(Sources 
    main.cpp
)

add_executable(${This} ${Headers} ${Sources})
