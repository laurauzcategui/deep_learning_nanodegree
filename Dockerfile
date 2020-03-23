FROM nvidia/cuda:10.0-base-ubuntu16.04

# Install some basic utilities
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
 && rm -rf /var/lib/apt/lists/*

# Create a working directory
ARG user=udacity
ARG datadir=/data

RUN mkdir $datadir
WORKDIR $datadir

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' --shell /bin/bash $user \
 && chown -R $user:$user $datadir
RUN echo "${user} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER $user

# All users can use /home/user as their home directory
ENV HOME=/home/$user
RUN chmod 777 /home/$user

# Install Miniconda
RUN curl -so ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-4.6.14-Linux-x86_64.sh \
 && chmod +x ~/miniconda.sh \
 && ~/miniconda.sh -b -p ~/miniconda \
 && rm ~/miniconda.sh
ENV PATH=$HOME/miniconda/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

# Create a Python 3.6 environment
RUN $HOME/miniconda/bin/conda config --append channels conda-forge
RUN $HOME/miniconda/bin/conda create -y --name py37 python=3.7.5 \
 && $HOME/miniconda/bin/conda clean -ya
ENV CONDA_DEFAULT_ENV=py37
ENV CONDA_PREFIX=$HOME/miniconda/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH
RUN $HOME/miniconda/bin/conda install conda-build=3.18.9=py37_5 \
 && $HOME/miniconda/bin/conda clean -ya

# CUDA 10.1-specific steps
ENV pycuda_version=py3.7_cuda10.1.243_cudnn7.6.3_0
ENV pytorch_version=1.3.1
ENV torchvision=0.4.2
ENV torchvision_cuda=py37_cu101


RUN conda install -y -c pytorch \
    cudatoolkit=10.1 \
    "pytorch=$pytorch_version=$pycuda_version" \
    "torchvision=$torchvision=$torchvision_cuda" \
 && conda clean -ya

# Install Torchnet, a high-level framework for PyTorch
RUN pip install torchnet==0.0.4

# Install Requests, a Python library for making HTTP requests
RUN conda install -y requests=2.19.1 \
 && conda clean -ya

# Install Graphviz
RUN conda install -y graphviz=2.40.1 python-graphviz=0.8.4 \
 && conda clean -ya

# Install OpenCV3 Python bindings
RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    libgtk2.0-0 \
    libcanberra-gtk-module \
 && sudo rm -rf /var/lib/apt/lists/*
RUN conda install -y -c conda-forge opencv=3.4.8 \
 && conda clean -ya

RUN conda install -y -c conda-forge jupyter matplotlib \
 && conda clean -ya

RUN conda install -y -c conda-forge pillow"<7.0.0" && conda clean -ya

RUN sudo apt update && \
    sudo apt install -y libgl1-mesa-glx

VOLUME $datadir

# Set the default command to jupyter notebook
CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/data --ip 0.0.0.0 --port=8888 --no-browser --allow-root"]

