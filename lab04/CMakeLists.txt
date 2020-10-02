# header begin
cmake_minimum_required(VERSION 3.16.6)
project(CS323_Compilers_lab04_json LANGUAGES C)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -lfl -ly")
# -fPIC
FIND_PACKAGE(FLEX REQUIRED)
FIND_PACKAGE(BISON REQUIRED)
FLEX_TARGET(lexer
    lex.l ${CMAKE_CURRENT_BINARY_DIR}/lex.yy.c)
BISON_TARGET(parser
    syntax.y ${CMAKE_CURRENT_BINARY_DIR}/syntax.tab.c)
ADD_FLEX_BISON_DEPENDENCY(lexer parser)


ADD_LIBRARY(${PROJECT_NAME}_lexer
     SHARED
     ${CMAKE_CURRENT_BINARY_DIR}/lex.yy.c
)

add_executable(
    ${PROJECT_NAME}_jp.out
     ./syntax.tab.c)

TARGET_LINK_LIBRARIES(${PROJECT_NAME}_jp.out ${PROJECT_NAME}_lexer)
