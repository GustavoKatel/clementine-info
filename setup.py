from setuptools import setup

setup(
    name = "clementineInfo",
    version = "0.0.1",
    author = "Gustavo Sampaio",
    author_email = "gbritosampaio@gmail.com",
    description = ("Python script to extract current track information "
            "from Clementine Music Player"),
    license = "GPLv2",
    keywords = "clementine player song dbus",
    url = "https://github.com/GustavoKatel/clementine-info",
    packages=['clementineInfo'],
    scripts = [
        'scripts/clementine-info'
    ]
)
