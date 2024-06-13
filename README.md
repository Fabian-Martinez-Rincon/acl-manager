<h1 align="center">ACL Manager <img
src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32" /></h1>



Proyecto para poder gestionar ACLs (Access Control List) en un entorno Linux, al tener muchos comandos repetidos basados en un excel se me ocurrio que seria mas comodo poder formater los comandos de forma automatica usando una interfaz "Amigable".

## ✏️ Interfaz

![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/476e6921-7b13-475e-9ae3-9389d4fc4ad1)

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

Instalamos las dependencias

```bash
pip install -r requirements.txt
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

### Seteamos de forma Recursiva

Antes de setear

```bash
redes@debian:~/Desktop$ ls -l /home/redes/Desktop
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
redes@debian:~/Desktop$ ls -l /home/redes/Desktop
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