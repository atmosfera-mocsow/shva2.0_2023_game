1. Устноваить зависимости

```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
# открыть новый терминал после этого

micromamba env create -f env.yml -y
micromamba activate pygame-env
# pip install pygame
```
2. Установить полезные плагины: VSCode - Расширения - Фильтрация - Рекомендованные для воркспейса
5. Запустить игру

```bash
python main.py
```
