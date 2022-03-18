from conans import ConanFile, RunEnvironment, tools
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class FailConan(ConanFile):
    name = "fail-test-case"
    version = "0.0.1"
    license = "Apache-2.0"
    tool_requires = ("cmake/3.22.3")
    requires = ("openssl/1.1.1m")
    settings = "os", "compiler", "build_type", "arch"
    description = ""

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        env_build = RunEnvironment(self)
        with tools.environment_append(env_build.vars):
            cmake = CMake(self)
            cmake.configure()
            cmake.build()
