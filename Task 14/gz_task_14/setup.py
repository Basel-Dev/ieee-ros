from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'gz_task_14'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
        glob('launch/*')),
        (os.path.join('share', package_name, 'worlds'),
            glob('worlds/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='basel-atef',
    maintainer_email='baseldevv@gmail.com',
    description='Task 14 Pkg',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'autonomous_rover = gz_task_14.autonomous_rover:main',
        ],
    },
)
