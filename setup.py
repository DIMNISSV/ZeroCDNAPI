from setuptools import setup

with open('README.md', encoding='UTF-8') as readme:
    long_description = readme.read()
with open('requirements.txt', encoding='UTF-8') as requirements:
    install_requires = requirements.read()
setup(
    name='ZeroCDN',
    version='1.0.6',
    long_description=long_description,
    author='dimnissv',
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Typing :: Typed',
    ],
    install_requires=install_requires,
)
