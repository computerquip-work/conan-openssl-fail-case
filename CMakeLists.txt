cmake_minimum_required(VERSION 3.20)

project(fail)

# This should work fine
find_package(OpenSSL REQUIRED)

# However, this does not. Instead, the OpenSSL_FOUND variable is defined
# instead. External code that calls find_package and relies on
# OPENSSL_FOUND fails as a result.
if (OPENSSL_FOUND)
    message(STATUS "1 The standard CMake OPENSSL_FOUND is defined.")
endif()

if (OpenSSL_FOUND)
    message(STATUS "2 The newer OpenSSL OpenSSL_FOUND is defined.")
endif()
