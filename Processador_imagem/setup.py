from setuptools import setup, find_packages

with open("Readme.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="image_processing",
    version="0.0.1",
    author="Juliane",
    author_email="qualqueremail@g.com.br",
    description="Projeto para aula DIO (aula que é uma porcaria)",
    packages=find_packages(),   
    pyhhon_requires='>=3.5',
)