import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ChecklistCombobox",
    version="1.1",
    author="Roger Hatfull",
    author_email="rogerhatfull@gmail.com",
    description="A Tkinter widget that uses Checkbutton widgets inside a Combobox widget",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hatfullr/ChecklistCombobox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)