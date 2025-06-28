# py_environment_setup.md

## Conda Installation and Setup

During Anaconda Install, you'll eventually get to a screen that asks if you would like to set your PATH environment variable using the installation wizard. Do NOT check this box. Leave BOTH boxes are unchecked.

RESIST this next step unless you need it. It seems I've not needed to do this yet...After installing Anaconda3, add to path:

```cmd
C:\Users\garth\anaconda3
C:\Users\garth\anaconda3\Scripts
```

Initialize in bash:
```bash
conda init bash  # close git and reopen
```

Update conda and all:
```bash
conda update conda
conda update anaconda
```

## Virtual Environments

### Python venv
```bash
python3.8 -m venv ocrenv2
source ocrenv2/bin/activate
python3.8 -m pip install --upgrade pip
```

### Conda Environments

Create conda virtual environment:
```bash
conda create -n dev python=3.7 anaconda
conda create --name dev python=3.7 anaconda
conda activate dev
```

List conda environments:
```bash
conda env list
conda list tensorflow
conda info -e  # what's this?
```

Someday when you're ready to update conda on VM:
```bash
conda update --force conda
conda update anaconda
conda update conda
conda update --all
conda install(?) spyder=5.0.0
```

## Specialized Environments

### AI Environment
```bash
conda create --name ai python=3.7 anaconda
pip install --upgrade tensorflow  # The TensorFlow 2.0 package has several dependencies which should already be installed in the default conda environment
conda list tensorflow  # 2.5 or higher
conda list keras  # Keras is a popular deep learning framework that serves as a high-level API for TensorFlow. Keras is now included with TensorFlow 2.0, so run the following command to verify that the package is available:
```

### NLP Environment
```bash
conda create --name blockchainenv python=3.7 anaconda
conda create --name nlpenv2 python=3.7 anaconda
python -c "import nltk;nltk.download('all')" -y
conda install -c conda-forge wordcloud -y
conda list wordcloud
pip install newsapi-python==0.2.5
conda list ibm-watson
conda install -c conda-forge spacy -y
python -m spacy download en_core_web_sm
conda list spacy
pip install alpaca-trade-api
```

### PyViz Environment
```bash
conda update anaconda
conda create -n pyvizenv python=3.7 anaconda -y
conda activate pyvizenv
pip install python-dotenv
conda install -c anaconda nb_conda -y
conda install -c conda-forge nodejs=12 -y
conda install -c pyviz holoviz -y
conda install -c plotly plotly -y
conda install -c conda-forge jupyterlab=2.2 -y
pip install numpy==1.19
pip install matplotlib==3.0.3
pip install pandas==1.1.5
set NODE_OPTIONS=--max-old-space-size=4096
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install jupyterlab-plotly --no-build
jupyter labextension install plotlywidget --no-build
jupyter labextension install @pyviz/jupyterlab_pyviz --no-build
jupyter lab build
set NODE_OPTIONS=  # correct
```

## Environment Variables

### Loading Environment Variables
```python
import os  # for loading env variables
from dotenv import load_dotenv  # for loading env variables. pip install python-dotenv
from pathlib import Path

home = Path.home() / ".env"  # windows 1/2
load_dotenv(home)  # windows 2/2
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
# path = "C:/users/garth/.env"
```

### Reading Environment Variables as Dictionary
```python
json_headers = {
    "Content-Type": "application/json",
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}
```

## Package Management

### Requirements Generation

Determine requirements with pipreqs:
```cmd
PS C:\lab_new\edge_raider> pipreqs
INFO: Successfully saved requirements file in C:\lab_new\edge_raider\requirements.txt
```

Also using pip freeze:
```bash
pip freeze
```

## Best Practices

1. **Always use virtual environments** for project isolation
2. **Pin specific versions** in requirements.txt for reproducibility
3. **Use environment variables** for sensitive configuration
4. **Document environment setup** in your project README
5. **Keep environments lean** - only install what you need