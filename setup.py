from setuptools import setup

setup(
    entry_points={
        "console_scripts": [
            "resnet = resnet_detector.__main__:main",
        ]
    }
)
