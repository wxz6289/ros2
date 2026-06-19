```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
conda --version
```

```sh
conda create -n robo_sim python=3.8 -y
conda activate robo_sim
conda install -c conda-forge gazebo -y
conda config --add channels conda-forge
conda config --set channel_priority strict
conda deactivate
conda env list
conda init zsh
conda config --set auto_activate_base false
```

```sh
# 删除环境
conda remove -n robo_sim --all -y
```

```sh
# 导出环境
conda env export > robo_sim_env.yaml
# 复现环境
conda env create -f robo_sim_env.yaml
```

```sh
conda create -n mujoco_env python=3.10 -y
conda activate mujoco_env
conda install mujoco gymnasium
```

```sh
conda create -n mujoco_env python=3.14.2 -y
conda activate mujoco_env
pip install mujoco
```