# RightVisuals Launcher v0.2.0

Прототип лаунчера для Minecraft Java Edition:
- Зафиксированная целевая версия Minecraft: **1.21.11**
- Загрузчик: **Fabric**
- Windows 10/11
- Сборка `.exe` локально или автоматически через GitHub Actions.

## Загрузка в GitHub
1. Создай новый пустой репозиторий GitHub, например `rightvisuals-launcher`.
2. Распакуй архив и загрузи **содержимое** папки в корень репозитория.
3. Открой вкладку **Actions** и запусти workflow `Build Windows EXE` через `Run workflow`.
   Также сборка автоматически запускается при push в `main`/`master`.
4. Открой завершённый запуск workflow, найди раздел **Artifacts** и скачай
   `RightVisualsLauncher-Windows`. Внутри будет `RightVisualsLauncher.exe`.

## Локальная сборка
На Windows с установленным Python 3.10+ запусти `build_exe.bat`.
Готовый файл появится в `dist/RightVisualsLauncher.exe`.

## Важное ограничение этой версии
Это пока интерфейс-прототип. Кнопка открывает официальный Minecraft Launcher.
Она не выполняет вход Microsoft, не устанавливает Fabric автоматически,
не скачивает Minecraft и не применяет выбранный RAM. Для игры заранее установи
официальный Minecraft Launcher и профиль Fabric для Minecraft 1.21.11.

Не запрашивай и не сохраняй пароли Microsoft. Для полноценного стороннего
лаунчера нужна безопасная реализация Microsoft OAuth и соблюдение правил
Microsoft/Mojang. Перед публикацией получи разрешение владельца бренда RightVisuals.
Проект не связан с Microsoft или Mojang.
