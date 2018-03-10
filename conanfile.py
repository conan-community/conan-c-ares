import os
from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment


class CAresConan(ConanFile):
    name = "c-ares"
    version = "1.14.0"
    license = "MIT"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "A C library for asynchronous DNS requests"
    website = "https://c-ares.haxx.se/"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx

    @property
    def folder_name(self):
        return "c-ares-cares-%s" % self.version.replace(".", "_")

    def source(self):
        ver = self.version.replace(".", "_")
        tools.get("https://github.com/c-ares/c-ares/archive/cares-%s.tar.gz" % ver)

    def _patch_cmake(self):
        conan_magic_lines = '''
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP()
'''
        tools.replace_in_file(os.path.join(self.source_folder, self.folder_name, "CMakeLists.txt"),
                              "PROJECT (c-ares C)",
                              "PROJECT (c-ares C)\n%s" % conan_magic_lines)

    def build(self):
        self._patch_cmake()
        cmake = CMake(self)
        cmake.definitions["CARES_STATIC"] = "ON" if not self.options.shared else "OFF"
        cmake.definitions["CARES_SHARED"] = "ON" if self.options.shared else "OFF"
        cmake.definitions["CARES_BUILD_TESTS"] = "OFF"
        cmake.configure(source_folder=self.folder_name)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*LICENSE*", dst="")

    def package_info(self):
        self.cpp_info.libs.append("cares")
