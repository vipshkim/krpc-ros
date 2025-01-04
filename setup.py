from setuptools import find_packages, setup

package_name = 'krpcros'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shinhyung',
    maintainer_email='vipsh.kim@gmail.com',
    description='connect krpc as simulator',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'conn=krpcros.member_function:main',
        ],
    },
)
