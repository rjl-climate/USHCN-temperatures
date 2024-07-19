from pathlib import Path


def define_env(env):
    @env.macro
    def include_file(filepath):
        filepath = Path(__file__).parent / "python_ushcn" / "plots" / filepath
        with open(filepath, "r") as file:
            return file.read()
