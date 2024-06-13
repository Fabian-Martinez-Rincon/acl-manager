<h1 align="center">ACL Manager <img
src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32" /></h1>



Proyecto para poder gestionar ACLs (Access Control List) en un entorno Linux, al tener muchos comandos repetidos basados en un excel se me ocurrio que seria mas comodo poder formater los comandos de forma automatica usando una interfaz "Amigable".

## ✏️ Interfaz

![image](/assets/Readme.PNG)

### Setup Windows


Creamos el entorno Virtual

```bash
python -m venv .venv
```

Activamos el entorno Virtual

```bash
.venv\Scripts\activate
```

En caso de no tener permisos, utilizar
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Botones

### Consultar

```bash
getfacl /home/redes/Desktop
```

Resultador

```bash
# file: home/redes/Desktop
# owner: redes
# group: users
user::rwx
group::---
other::r-x
```

### Setear

```bash
setfacl -m g::--- /home/redes/Desktop; setfacl -m g:group1:rwx /home/redes/Desktop; setfacl -m g:group2:r-x /home/redes/Desktop; setfacl -m g:group3:--- /home/redes/Desktop
```

Consultamos el resultado

```bash
# file: home/redes/Desktop
# owner: redes
# group: users
user::rwx
group::---
group:group1:rwx
group:group2:r-x
group:group3:---
mask::rwx
other::r-x
```