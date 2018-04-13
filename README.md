[![Download](https://api.bintray.com/packages/conan-community/conan/c-ares%3Aconan/images/download.svg?version=1.14.0%3Astable) ](https://bintray.com/conan-community/conan/c-ares%3Aconan/1.14.0%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-c-ares.svg?branch=release%2F1.14.0)](https://travis-ci.org/conan-community/conan-c-ares)
[![Build status](https://ci.appveyor.com/api/projects/status/github/conan-community/conan-c-ares?svg=true)](https://ci.appveyor.com/project/conan-community/conan-c-ares)

# conan-c-ares

![Conan C Ares](logo.png)

## Conan package for C Ares.

### Basic setup

    $ conan install c-ares/1.14.0@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    c-ares/1.14.0@conan/stable

    [options]
    c-ares:shared=true # false

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:

    conan install .

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

## License

[MIT License](LICENSE)
