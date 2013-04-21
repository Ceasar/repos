from setuptools import setup

__version_info__ = ('0', '0', '1')
__version__ = '.'.join(__version_info__)


setup(
    name="repos",
    version=__version__,
    description="Batch Git repository manager",
    author="Ceasar Bautista",
    author_email="cbautista2010@gmail.com",
    url="http://www.github.com/Ceasar/repos",
    py_modules=["repos"],
    install_requires=["fabric"]
)
