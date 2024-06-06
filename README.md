<h1 align="center">ACL Manager <img
src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32" /></h1>



Proyecto para poder gestionar ACLs (Access Control List) en un entorno Linux, al tener muchos comandos repetidos basados en un excel se me ocurrio que seria mas comodo poder formater los comandos de forma automatica usando una interfaz "Amigable".

## ✏️ Dependencias

![image](https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/409f30b6-4571-4bdd-ad15-29366fc9c563)

### Proceso de configuracion

Consultar grupos creados

```bash
getent group
```

Crear todos los grupos necesarios

```bash
for group in group1 group2 group3; do sudo groupadd $group; done
```

Consultar usuarios creados

```bash
for group in group1 group2 group3; do getent group $group || echo "Group $group does not exist"; done
```

Eliminar todos los grupos creados

```bash
for group in group1 group2 group3; do sudo groupdel $group; done
```

Para asignar un usuario a varios grupos

```bash
sudo usermod -a -G group1,group2,group3 username
```

Para crear varios usuarios

```bash
for user in user1 user2 user3; do sudo adduser $user; done
```

Consultar usuarios creados

```bash
cut -d: -f1 /etc/passwd
```
