# API Github
> Essa API foi desenvolvido em python utilizando o micro-framework Flask

## Utilização da API

Para utilizar a API segue um exemplo utilizando o curl:

Inicar a aplicação:
```bash
$ flask run
```

Em outro terminal:

```bash
$ curl -X POST localhost:5000/api/v1/user -d \
'{"username": "yourusername"}'
```

## Para visualização web

1. Inicie a aplicação
2. Acesse o localhost:5000 e repasse o seu username