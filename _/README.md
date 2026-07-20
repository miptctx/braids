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

# Сборка vitepress
Инициализация репозитория делается один раз.
```bash
cd _
docker run -it -v .:/app --entrypoint bash node:latest
cd app
npm add -D vitepress
npm add -D markdown-it-mathjax3
npx vitepress init
# add any other dependencies and project parameters
```

Локально vitepress собирается и деплоится так.
```bash
cd _
docker run -it -v .:/app --entrypoint bash node:latest
cd /app
npm run docs:build
# push it to the vitepress hosting
vercel --prod .vitepress/dist
```

# Описание файлов
См. [index.md](index.md).
