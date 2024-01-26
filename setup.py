import setuptools

setuptools.setup(
    name='bar',
    version='1.0.0',
    author='karim@gheddache.com',
    description='Prévision Lounge à 14 jours',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn==1.3",
        "pandas==2.1.2"
    ]
)