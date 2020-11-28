cmake_minimum_required(VERSION 3.10)

project(BuildSystemsFun CXX)

find_package(Doxygen)

set(MAIN_SOURCE b/main.cpp)

add_executable(BuildSystemsFun ${MAIN_SOURCE})

add_subdirectory(a)

add_custom_command(
        OUTPUT index.h
        WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/c
        COMMAND python preparing.py
        COMMENT "Generating c/index.h"
        VERBATIM
)
add_custom_target(PreparingIndex DEPENDS index.h COMMENT "Checking if re-generation is required")
add_dependencies(BuildSystemsFun PreparingIndex)

add_custom_target(
        doc ALL
        COMMAND doxygen -g Doxyfile && doxygen Doxyfile
        WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/doc
        COMMENT "Generating documentation with Doxygen"
        VERBATIM
)

target_compile_options(BuildSystemsFun PUBLIC -std=c++14)
target_link_libraries(BuildSystemsFun PUBLIC ALibrary)
target_include_directories(BuildSystemsFun PUBLIC ${PROJECT_SOURCE_DIR} b)
