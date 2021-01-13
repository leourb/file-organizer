import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="file_organizer",
    version="1.0.0",
    author="Leonardo Urbano",
    author_email="leonardo.urbano87@libero.it",
    packages=['file_organizer'],
    install_requires=['requests>=2.25.1', 'beautifulsoup4>=4.9.3'],
    description="Organizes the files in a folder following the same structure of FileInfo.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/leourb/file-organizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'organize=file_organizer.main:organize',
        ]
    }
)