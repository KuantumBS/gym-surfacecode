import setuptools

setuptools.setup(
      name='gym_surfacecode',
      version='0.0.1',
      packages=setuptools.find_packages(),
      package_dir={'gym_surfacecode'},
      package_data={'gym_surfacecode': ['envs/referee_decoder/X_decoder','envs/referee_decoder/DP_decoder']},
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)

