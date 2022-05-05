from setuptools import setup, find_packages
import pathlib


directory = pathlib.Path(__file__).parent

README = (directory / "README.md").read_text()

setup(
    name='gym_surfacecode',
    version='0.0.1',
    description='gym_surfacecode',
    long_description=README,
    long_description_content_type='text/markdown',
    package_dir={'gym_surfacecode'},
    package_data={'gym_surfacecode': ['envs/referee_decoder/X_decoder','envs/referee_decoder/DP_decoder']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    python_requires='>3.7.0',
)
