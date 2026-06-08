"""SpatialAgent 包安装配置。"""

from setuptools import setup, find_packages

setup(
    name="spatial-agent",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
