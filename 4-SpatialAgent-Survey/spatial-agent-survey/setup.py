"""Package setup for spatial-agent-survey."""

from setuptools import find_packages, setup


setup(
    name="spatial-agent-survey",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
