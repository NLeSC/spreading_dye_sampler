from setuptools import setup
setup(
        name = 'spreading_dye_sampler',
        packages = ['spreading_dye_sampler'],
        version = '0.1.0',
        description = 'Python implementation of the spreading dye algorithm',
        author = 'Lourens Veen',
        author_email = 'l.veen@esciencecenter.nl',
        url = 'https://github.com/NLeSC/spreading_dye_sampler',
        download_url = 'https://github.com/NLeSC/spreading_dye_sampler/archive/0.1.0.tar.gz',
        license = 'Apache License 2.0',
        python_requires='>=3.5.*, <4',
        install_requires=[
            'numpy'
            ],
        keywords = ['spreading dye', 'spatial sampling'],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'],
        )
