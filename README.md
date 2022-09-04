# Thread_list<br />
python class that make threading easier <br />

### First: crete a class object first<br />
if you want to thread over single function pass the function as parameter
> class_obj = Thread_list()

### Second: add thread to object<br />
> class_obj.add_tread(target, args, kwargs)
Signature<br />
```json
{
    "target": "callable",
    "args": "tuple",
    "kwargs": "dict"
}
```
### Third: call the object to run the tread<br />
join_trd: if you want to join the threads<br />
> class_obj(join_trd=False)
