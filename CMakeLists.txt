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
    #NUMPY_URL numpy/numpy-${REZ_BUILD_PROJECT_VERSION}-pp37-pypy37_pp73-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
    NUMPY_URL numpy/numpy-1.21.6-pp37-pypy37_pp73-manylinux_2_12_x86_64.manylinux2010_x86_64.whl 
    #https://files.pythonhosted.org/packages/2c/44/4210d16af96fe03f41c64bac2146435dc521a6e0457fdb3b5d15e1844578/numpy-${REZ_BUILD_PROJECT_VERSION}-pp37-pypy37_pp73-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
    https://files.pythonhosted.org/packages/2e/5a/6f3e280a10de48395053a559bfcb3b2221b74b57d062c1d6307fc965f549/numpy-1.21.6-pp37-pypy37_pp73-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
)

# In the case of a Python pip wheel file, we do not have any archive to extract, so we can just execute our Bash
# script(s) inside an "execute_process" macro.
execute_process(
    COMMAND
    bash ${CMAKE_SOURCE_DIR}/install.sh ${NUMPY_URL}
    RESULT_VARIABLE RETURN_CODE
)

# We check that the execute_process() macro terminated properly.
# If not, we abort the process.
if(RETURN_CODE EQUAL "1")
    message(FATAL_ERROR "[CMAKE] Install script returned an error code. Aborting...")
endif()

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] NumPy-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
