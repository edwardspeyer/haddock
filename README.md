# haddock

A cat database with the following features:
* sqlite3 as a backend datastore, exposed as an internal UDP service
* an HTTP frontend, for public use
* stores the following fields, keyed by cat `name`:
    * fur color

```
$ docker-compose up --detach
Creating network "haddock_default" with the default driver
Creating haddock_frontend_1 ... done
Creating haddock_backend_1  ... done

$ ./test
----
< POST george/brown
>
----
< GET george
> brown
----
< POST george/tabby
>
----
< GET george
> tabby
```
