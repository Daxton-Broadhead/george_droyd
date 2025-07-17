from setuptools import find_packages, setup

package_name = 'launch_files'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/launch_files']),
        ('share/launch_files', ['package.xml']),
        ('share/launch_files/launch', ['launch/launchfile.py']),
        ('share/launch_files/config', ['config/config_file.yaml']),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='daxton',
    maintainer_email='daxton.broadhead21@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
