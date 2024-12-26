
# Fast API

API 
## Execução:
  - pip install -r requirements.txt
    - uvicorn main:app --reload
## Referência

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Etiquetas

Adicione etiquetas de algum lugar, como: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Documentação da API


```http
  GET /api/
```
#### ()


```http
  GET /api/products/${id}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item |
#### read_item(id)

```http
  POST /api/products/${name}/${descripition}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `name` | `string` | **Obrigatório**. O novo nome do item |
| `descripition` | `string` | **Obrigatório**. A nova descrição do item |
#### create_item(name, descripition)

```http
  PUT /api/products/${id_item}/${name}/${descripition}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id_item`      | `string` | **Obrigatório**. O ID do item |
| `name`      | `string` | **Obrigatório**. O novo nome do item |
| `descripition`| `string` | **Obrigatório**. A nova descrição do item |
#### update_item(id_item, name, descripition)

```http
  DELETE /api/products/${id_item}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
|`id_item`| `string`|**Obrigatório**. O ID do item |
#### delete_item(id_item)
