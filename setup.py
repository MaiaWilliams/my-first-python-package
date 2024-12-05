from setuptools import setup, find_packages
from pathlib import Path

# Requirements
try:
  this_directory = Path(__file__).absolute().parent
  with open((this_directory / "requirements.txt"), encoding = "utf-8") as f:
    requirements = f.readlines()
  requirements = [line.strip() for line in requirements]
except FileNotFoundError:
  requirements = []

# Metadata
setup(
  name = "maiapy",
  version = "0.0.0.1000",
  author = "Maia Williams",
  author_email = "maia.williams@plus.ac.at",
  description = "Python code prepared as part of PhD seminar workshop with Luuk on 5 December 2024. How to publish python code using GitHub.",
  license = "Luuk's license",
  packages = find_packages(),
  install_requires = requirements
)
