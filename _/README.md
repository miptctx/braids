# Запуск sage

Из корневой папки проекта:

```bash
docker run -it --rm --entrypoint bash -v .:/home/sage/code sagemath/sagemath:latest
```

# Запуск sage braids
Запускать надо из корневой папки проекта (braids):
```bash
docker run -it --rm --entrypoint bash -v .:/home/sage/code braids:latest
cd code/_/...
```

# Описание файлов
См. [index.md](index.md).
