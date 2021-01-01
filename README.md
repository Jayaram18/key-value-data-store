# CRD-operations-of-a-file-based-key-value-data-store.
![Build Status](https://img.shields.io/badge/Python-3.9-blue)
This is a file which can be exposed as a library that supports the basic CRD(create, read, write) operations. Data store is meant to local storage for one single process on single laptop.


The data store will support the following :
```sh
>>> import code as x
```
1. It can be initialized using an optional file path. If one is not provided, it will reliably 
create itself in a reasonable location on the laptop.

2. A new key-value pair can be added to the data store using the Create operation.
```sh
>>> x.create("one",1)
The key is always a string - capped at 32chars.
```

```sh
>>> x.create("andshrrljwhengdijsddlkfndiidknffpdjejd",8)
error: Key_name can contain only 32 characters
 The value is always a JSON object - capped at 16KB.
```
3. If Create is invoked for an existing key, an appropriate error must be returned.
```sh
>>> x.create("name",23)
error: this key already exists
```
4. A Read operation on a key can be performed by providing the key, and receiving the 
value in response, as a JSON object.
```sh
>>> x.read("one")
'one:1'
```
5. A Delete operation can be performed by providing the key.
```sh
>>> x.delete("one")
key is successfully deleted
```
6. Every key supports setting a Time-To-Live property when it is created. This property is
optional. If provided, it will be evaluated as an integer defining the number of seconds 
the key must be retained in the data store. Once the Time-To-Live for a key has expired, 
the key will no longer be available for Read or Delete operations.

7. Appropriate error responses must always be returned to a client if it uses the data store in 
unexpected ways or breaches any limits.
```sh
>>> x.create("name",67)
>>> x.modify("name",34)
>>> x.read("name")
'name:34'
```

8. The file size never exceeds 1GB.

9. The file is accessed by multi-threading.


