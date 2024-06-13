from setuptools import find_packages, setup

setup(
    name="touchid",
    packages=find_packages(),
    include_package_data=True,
    # py_modules=["touchid"],
    version="1.2.0",
    description="Access the Touch ID sensor",
    long_description="`touchid` provides an easy to use API for accessing the Touch ID sensor via Apple's LocalAuthentication framework",
    keywords=["touch-id", "LocalAuthentication", "LAContext"],
    license="MIT",
    author="Lukas Kollmer",
    author_email="lukas.kollmer@gmail.com",
    url="https://github.com/aajmorgan6/py-touch-id/",
    install_requires=["pyobjc-framework-LocalAuthentication"]
)
