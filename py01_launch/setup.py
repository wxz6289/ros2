from setuptools import find_packages, setup
from glob import glob

package_name = 'py01_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*_launch.py')),
        ('share/' + package_name + '/launch', glob('launch/*_launch.yml')),
        ('share/' + package_name + '/config', glob('config/*.yml')),

        # ('share/' + package_name, ['launch/py01_hello_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='dreamingking@live.cn',
    description='TODO: Package description',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
