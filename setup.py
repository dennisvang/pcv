import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='pcv',
    version="0.0.1",
    author='Dennis van Gerwen',
    author_email='dvg@email.com',
    description='Yet another package that creates a PDF resume (CV) from YAML '
                'or JSON.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dennisvang/pcv/',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
