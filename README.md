# Thread_list
python class that make threading easier 

First: crete a class object first<br />
if you want to thread over single function pass the function as parameter
> class_obj = Thread_list()

Second: add thread to object<br />
> class_obj.add_tread(target, args, kwargs)
> Signature
```json
{
    "target": "callable",
    "args": "tuple",
    "kwargs": "dict"
}
```
Third: call the object to run the tread<br />
join_trd: if you want to join the threads (all the threads Done)
> class_obj(join_trd=False)
