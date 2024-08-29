<h1 align="center">ACL Manager <img
src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32" /></h1>

Proyecto para poder gestionar ACLs (Access Control List) en un entorno Linux, al tener muchos comandos repetidos basados en un excel se me ocurrio que seria mas comodo poder formater los comandos de forma automatica usando una interfaz "Amigable".

https://github.com/Fabian-Martinez-Rincon/acl-manager/assets/55964635/629296ad-cf81-4db5-afb9-1d544a6e8d51

### ✏️ Interfaz

![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/476e6921-7b13-475e-9ae3-9389d4fc4ad1)

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

### ⚙️ Setup

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

Instalamos las dependencias

```bash
pip install -r requirements.txt
```

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

### 🔴 Botones

`Consultar`

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

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

`Setear`

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

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

`Seteamos de forma Recursiva`

Antes de setear

```bash
Comando: ls -l /home/redes/Desktop
total 18124
-rwxrwxrwx  1 redes users      205 May 21 07:57  convert_to_csv.py
-rwxrwxrwx  1 redes users      443 May 21 08:07  ejecutar_permisos.sh
drwxr-xr-x  4 redes users     4096 May 31 07:38  MartinezRincon-0d5ae8-main
-rw-rw-rw-  1 redes users    82968 May 31 06:46  MartinezRincon-0d5ae8-main.zip
-rw-rw-rw-  1 redes users    10282 May 21 06:50 'Permisos 2.0.xlsx'
-rw-r--r--  1 redes users     4345 May 21 07:57  permisos.csv
drwxr-xr-x 16 redes users     4096 May 31 07:02  Python-3.8.10
-rw-r--r--  1 redes users 18433456 May  3  2021  Python-3.8.10.tar.xz
```

Despues de setear

```bash
setfacl -R -m g::--- /home/redes/Desktop; setfacl -R -m g:group1:rwx /home/redes/Desktop; setfacl -R -m g:group2:r-x /home/redes/Desktop; setfacl -R -m g:group3:--- /home/redes/Desktop
```
```bash
Comando: ls -l /home/redes/Desktop
total 18124
-rwxrwxrwx+  1 redes users      205 May 21 07:57  convert_to_csv.py
-rwxrwxrwx+  1 redes users      443 May 21 08:07  ejecutar_permisos.sh
drwxrwxr-x+  4 redes users     4096 May 31 07:38  MartinezRincon-0d5ae8-main
-rw-rwxrw-+  1 redes users    82968 May 31 06:46  MartinezRincon-0d5ae8-main.zip
-rw-rwxrw-+  1 redes users    10282 May 21 06:50 'Permisos 2.0.xlsx'
-rw-rwxr--+  1 redes users     4345 May 21 07:57  permisos.csv
drwxrwxr-x+ 16 redes users     4096 May 31 07:02  Python-3.8.10
-rw-rwxr--+  1 redes users 18433456 May  3  2021  Python-3.8.10.tar.xz
```

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

`Eliminar`

Antes de eliminar los permisos

```bash
Comando: getfacl /home/redes/Desktop
getfacl: Removing leading '/' from absolute path names
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

Elimina los permisos actuales y los que tiene por defecto.

```bash
setfacl -b /home/redes/Desktop && setfacl -k /home/redes/Desktop
```

```bash
Comando: getfacl /home/redes/Desktop
getfacl: Removing leading '/' from absolute path names
# file: home/redes/Desktop
# owner: redes
# group: users
user::rwx
group::---
other::r-x
```

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

`Eliminar R` (De forma Recursiva)

Antes de eliminar los permisos

```bash
Comando: ls -l /home/redes/Desktop
total 18124
-rwxrwxrwx+  1 redes users      205 May 21 07:57  convert_to_csv.py
-rwxrwxrwx+  1 redes users      443 May 21 08:07  ejecutar_permisos.sh
drwxrwxr-x+  4 redes users     4096 May 31 07:38  MartinezRincon-0d5ae8-main
-rw-rwxrw-+  1 redes users    82968 May 31 06:46  MartinezRincon-0d5ae8-main.zip
-rw-rwxrw-+  1 redes users    10282 May 21 06:50 'Permisos 2.0.xlsx'
-rw-rwxr--+  1 redes users     4345 May 21 07:57  permisos.csv
drwxrwxr-x+ 16 redes users     4096 May 31 07:02  Python-3.8.10
-rw-rwxr--+  1 redes users 18433456 May  3  2021  Python-3.8.10.tar.xz
```

Elimina los permisos actuales y los que tiene por defecto de forma recursiva.

```bash
setfacl -R -b /home/redes/Desktop && setfacl -R -k /home/redes/Desktop
```

```bash
Comando: ls -l /home/redes/Desktop
total 18124
-rwx---rwx  1 redes users      205 May 21 07:57  convert_to_csv.py
-rwx---rwx  1 redes users      443 May 21 08:07  ejecutar_permisos.sh
drwx---r-x  4 redes users     4096 May 31 07:38  MartinezRincon-0d5ae8-main
-rw----rw-  1 redes users    82968 May 31 06:46  MartinezRincon-0d5ae8-main.zip
-rw----rw-  1 redes users    10282 May 21 06:50 'Permisos 2.0.xlsx'
-rw----r--  1 redes users     4345 May 21 07:57  permisos.csv
drwx---r-x 16 redes users     4096 May 31 07:02  Python-3.8.10
-rw----r--  1 redes users 18433456 May  3  2021  Python-3.8.10.tar.xz
```

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

`Setear Por Defecto`

Antes de setear

```bash
Comando: getfacl /home/redes/Desktop
getfacl: Removing leading '/' from absolute path names
# file: home/redes/Desktop
# owner: redes
# group: users
user::rwx
group::---
other::r-x
```

Seteamos los permisos por defecto

```bash
setfacl -d -m g::--- /home/redes/Desktop; setfacl -d -m g:group1:rwx /home/redes/Desktop; setfacl -d -m g:group2:r-x /home/redes/Desktop; setfacl -d -m g:group3:--- /home/redes/Desktop
```

```bash
Comando: getfacl /home/redes/Desktop
getfacl: Removing leading '/' from absolute path names
# file: home/redes/Desktop
# owner: redes
# group: users
user::rwx
group::---
other::r-x
default:user::rwx
default:group::---
default:group:group1:rwx
default:group:group2:r-x
default:group:group3:---
default:mask::rwx
default:other::r-x
```

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

`Setear` Por Defecto de Forma Recursiva

Antes de setear

```bash
ls -l /home/redes/Desktop
total 18124
-rwx---rwx  1 redes users      205 May 21 07:57  convert_to_csv.py
-rwx---rwx  1 redes users      443 May 21 08:07  ejecutar_permisos.sh
drwx---r-x  4 redes users     4096 May 31 07:38  MartinezRincon-0d5ae8-main
-rw----rw-  1 redes users    82968 May 31 06:46  MartinezRincon-0d5ae8-main.zip
-rw----rw-  1 redes users    10282 May 21 06:50 'Permisos 2.0.xlsx'
-rw----r--  1 redes users     4345 May 21 07:57  permisos.csv
drwx---r-x 16 redes users     4096 May 31 07:02  Python-3.8.10
-rw----r--  1 redes users 18433456 May  3  2021  Python-3.8.10.tar.xz
```

Seteamos los permisos por defecto de forma recursiva (Solo se aplica en directorios)

```bash
setfacl -R -d -m g::--- /home/redes/Desktop; setfacl -R -d -m g:group1:rwx /home/redes/Desktop; setfacl -R -d -m g:group2:r-x /home/redes/Desktop; setfacl -R -d -m g:group3:--- /home/redes/Desktop
```

```bash
ls -l /home/redes/Desktop
total 18124
-rwx---rwx   1 redes users      205 May 21 07:57  convert_to_csv.py
-rwx---rwx   1 redes users      443 May 21 08:07  ejecutar_permisos.sh
drwx---r-x+  4 redes users     4096 May 31 07:38  MartinezRincon-0d5ae8-main
-rw----rw-   1 redes users    82968 May 31 06:46  MartinezRincon-0d5ae8-main.zip
-rw----rw-   1 redes users    10282 May 21 06:50 'Permisos 2.0.xlsx'
-rw----r--   1 redes users     4345 May 21 07:57  permisos.csv
drwx---r-x+ 16 redes users     4096 May 31 07:02  Python-3.8.10
-rw----r--   1 redes users 18433456 May  3  2021  Python-3.8.10.tar.xz
```

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">