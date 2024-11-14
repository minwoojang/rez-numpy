name = "numpy"

version = "1.12.1"

authors = [
    "Travis E. Oliphant et al."
]

description = \
    """
    NumPy is the fundamental package for array computing with Python.
    """

requires = [
    "cmake",
    "pip-21.3",
    "python-3.7"
]

variants = [
    ['platform-linux', 'arch-x86_64']
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "numpy-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}")

    # Helper environment variables.
    env.NUMPY_BINARY_PATH.set("{root}/bin")
    env.NUMPY_INCLUDE_PATH.set("{root}/numpy/core/include")
    env.NUMPY_LIBRARY_PATH.set("{root}/numpy/core/lib")
