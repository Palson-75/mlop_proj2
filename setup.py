import setuptools

__version__ = "0.0.0"

REPO_NAME = "mlop_proj2"
AUTHOR_USER_NAME = "Palson-75"
SRC_REPO = "project1"
AUTHOR_EMAIL = "chinnugarnipudi555@gmail.com"

long_description = "MLOps project"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)