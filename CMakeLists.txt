cmake_minimum_required(VERSION 3.10)

project(BuildSystemsFun CXX)

add_custom_command(
        OUTPUT include.h
        COMMAND python3 ${PROJECT_SOURCE_DIR}/c/preparing.py ${PROJECT_SOURCE_DIR}
        COMMENT "Generating a header."
)

set(MAIN_SOURCE b/main.cpp)

add_custom_target(Preparing DEPENDS include.h COMMENT "Checking if re-generation is required")

add_custom_target(
        doc ALL
        COMMAND doxygen -g Doxyfile && doxygen Doxyfile
        WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/doc
        COMMENT "Generating documentation with Doxygen"
)

include_directories(a c)

add_executable(BuildSystemsFun ${MAIN_SOURCE})
add_subdirectory(a)
add_dependencies(BuildSystemsFun Preparing)


target_compile_options(BuildSystemsFun PUBLIC -std=c++14)
target_link_libraries(BuildSystemsFun PUBLIC ALibrary)
target_include_directories(BuildSystemsFun INTERFACE
        "${PROJECT_BINARY_DIR}/a"
        "${PROJECT_BINARY_DIR}/b"
        "${PROJECT_BINARY_DIR}/c"
        )

install(
        TARGETS BuildSystemsFun
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
)
