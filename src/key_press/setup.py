from setuptools import find_packages, setup

package_name = 'key_press'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/sounds', ['sounds/yeetSound.mp3']),
    ],
    install_requires=['playsound', 'setuptools'],
    zip_safe=True,
    maintainer='daxton',
    maintainer_email='daxton.broadhead21@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'play_sound = key_press.sound:main'
        ],  
    },
)
