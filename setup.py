from setuptools import setup, find_packages

setup(
    name="POC of Sphinx",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy==1.26.4",
        "pytest==7.0.1",
    ],
    python_requires=">=3.12",
    author="Benjamin",
    description="POC of Sphinx",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={  # script exécutable
        "console_scripts": [
            "vehicles=vehicles.main:main",  # Exécutable CLI to run project
        ],
    },
)