CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# NumPy
rez_set_archive(
    # This is a relative path from the ${REZ_REPO_PAYLOAD_DIR} environment variable,
    # that is pointing to the root directory where we can find all the archives of the package
    # we can build, using the following hierarchy:
    # "${REZ_REPO_PAYLOAD_DIR}/project_name/archive.what.ever"
    NUMPY_URL numpy/numpy-${REZ_BUILD_PROJECT_VERSION}-cp27-cp27mu-manylinux1_x86_64.whl
    https://files.pythonhosted.org/packages/f9/d5/f24f86b51298f171826a398efdd64b5214b687a28a2f05ff736b1505b1b2/numpy-${REZ_BUILD_PROJECT_VERSION}-cp27-cp27mu-manylinux1_x86_64.whl
)

# In the case of a Python pip wheel file, we do not have any archive to extract, so we can just execute our Bash
# script(s) inside an "execute_process" macro.
execute_process(
    COMMAND
    bash ${CMAKE_SOURCE_DIR}/install.sh ${NUMPY_URL}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] NumPy-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
