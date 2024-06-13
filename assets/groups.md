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