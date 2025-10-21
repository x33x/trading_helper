from setuptools import setup, find_packages

setup(
    name="trading_helper",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests"  # API requests
    ],
    python_requires=">=3.9",
)

