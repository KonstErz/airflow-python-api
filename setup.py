from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='airflow-python-api',
  version='1.0.0',
  author='KonstErz',
  author_email='konstantin.yerzin@gmail.com',
  description='Python package for interacting with Airflow API (Stable)',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/KonstErz/airflow-python-api',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.10',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='airflow python api',
  project_urls={
    'Documentation': 'https://github.com/KonstErz/airflow-python-api'
  },
  python_requires='>=3.6'
)
