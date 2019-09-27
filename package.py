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
    "cmake-3",
    "gcc-6",
    "python-2.7"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

#TODO: Use the SHA1 of the archive instead.
uuid = "numpy-1.12.1"

def commands():
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}")