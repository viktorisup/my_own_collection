# my_own_module

## Описание

Модуль `my_own_module` предназначен для создания и обновления текстовых файлов с заданным содержимым. Если файл с указанным путем уже существует, модуль проверяет его содержимое и, при необходимости, обновляет его.

## Аргументы

- **path** (строка, обязательный):
  Путь к файлу, который нужно создать или обновить.

- **content** (строка, обязательный):
  Содержимое, которое должно быть записано в файл.

## Возвращаемые значения

- **message** (строка):
  Сообщение, описывающее результат выполнения операции. Может содержать следующие значения:
  - "File content updated." — содержимое файла было обновлено.
  - "Created a new file with the given content." — файл был успешно создан.
  - "A file with this content already exists. Creation is not required." — файл с таким содержимым уже существует.
  - "Wrong path. File not accessible." — указанный путь недоступен.

## Пример использования

### Пример 1: Создание нового файла

```yaml
- name: Create a new file with specific content
  hosts: localhost
  tasks:
    - name: Use my_own_module to create a new file
      my_own_module:
        path: "/tmp/new_file.txt"
        content: "Hello, world!"