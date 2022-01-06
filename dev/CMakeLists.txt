################################################################################
# The following development macros are used for debugging within the projects
# CMake files. These functions are defined early in the CMake build process.
################################################################################

################################################################################
# Debug Macro: print_all_variables()
################################################################################
macro(print_all_variables)
    message(STATUS "//////////////////////////////////////////////////////////")
    get_cmake_property(_variableNames VARIABLES)
    foreach (_variableName ${_variableNames})
        message(STATUS "// ${_variableName}=${${_variableName}}")
    endforeach()
    message(STATUS "//////////////////////////////////////////////////////////")
endmacro()
################################################################################