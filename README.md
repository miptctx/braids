# Sage в докере
**First run**
```bash
docker run -it --rm --entrypoint bash -v .:/home/sage/code -t braids sagemath/sagemath:latest
cd code
sage -pip install -e .
```

**Commit**
```bash
docker commit braids braids:latest
```

**Next runs**
```bash
docker run -it --rm --entrypoint bash -v .:/home/sage/code braids:latest
cd code
```

# Sage на хосте
Sage не использует вирутальную среду, у нее свой питон и своя среда.

Чтобы установить пакет в виртуальную среду надо выполнить
```bash
sage -pip install -e .
```

