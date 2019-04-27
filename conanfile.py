#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools


class CAresConan(ConanFile):
    name = "c-ares"
    version = "1.14.0"
    license = "MIT"
    url = "https://github.com/conan-community/conan-c-ares"
    description = "A C library for asynchronous DNS requests"
    author = "lasote"
    homepage = "https://c-ares.haxx.se/"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {'shared': False, 'fPIC': True}
    exports = "LICENSE"
    exports_sources = "CMakeLists.txt"
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        ver = self.version.replace(".", "_")
        tools.get("https://github.com/c-ares/c-ares/archive/cares-%s.tar.gz" % ver)

    def cmake_configure(self):
        cmake = CMake(self)
        cmake.definitions["CARES_STATIC"] = not self.options.shared
        cmake.definitions["CARES_SHARED"] = self.options.shared
        cmake.definitions["CARES_BUILD_TESTS"] = "OFF"
        cmake.definitions["CARES_MSVC_STATIC_RUNTIME"] = "OFF"
        # Do not mess with runtime, Conan will.
        if self.settings.os != "Windows":
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = self.options.fPIC or self.options.shared
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.cmake_configure()
        cmake.build()
        cmake.install()

    def package(self):
        cmake = self.cmake_configure()
        cmake.install()
        self.copy("*LICENSE.md", src=self.source_folder, dst="licenses", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if not self.options.shared:
            self.cpp_info.defines.append("CARES_STATICLIB")
        if self.settings.os == "Windows":
            self.cpp_info.libs.append("ws2_32")
