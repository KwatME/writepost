from setuptools import find_packages, setup

na = "md_post"

setup(
    name=na,
    version="0.4.0",
    url="https://github.com/KwatME/md_post",
    python_requires=">=3.6.0",
    install_requires=["click", "pyyaml"],
    packages=find_packages(),
    entry_points={"console_scripts": ["{0}={0}.{1}:{1}".format(na, "cli")]},
)
