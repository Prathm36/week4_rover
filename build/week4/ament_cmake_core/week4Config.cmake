# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_week4_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED week4_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(week4_FOUND FALSE)
  elseif(NOT week4_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(week4_FOUND FALSE)
  endif()
  return()
endif()
set(_week4_CONFIG_INCLUDED TRUE)

# output package information
if(NOT week4_FIND_QUIETLY)
  message(STATUS "Found week4: 0.0.0 (${week4_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'week4' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${week4_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(week4_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${week4_DIR}/${_extra}")
endforeach()
