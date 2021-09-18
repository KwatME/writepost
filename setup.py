from setuptools import find_packages, setup

na = "md_post"

setup(
    name=na,
    version="0.5.0",
    url="https://github.com/KwatME/md_post",
    python_requires=">=3.6.0",
    install_requires=["click", "pyyaml"],
    packages=find_packages(),
    entry_points={"console_scripts": ["{0}={1}.{2}:{2}".format(na.replace("_", "-"), na, "cli")]},
)
