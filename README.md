# pyinfraql - Python Library for InfraQL

> __*This repository has been archived.  The active project is now located at [PyStackQL](https://github.com/stackql/pystackql)*__

![Platform Support](https://img.shields.io/badge/platform-windows%20macos%20linux-brightgreen)
![Python Support](https://img.shields.io/badge/python-3.6%2B-brightgreen)

Python wrapper for InfraQL

## Usage

```python
from pyinfraql import InfraQL  
iql = InfraQL(keyfilepath='/tmp/infraql-demo.json')
results = iql.execute("SHOW SERVICES IN google")
print(results)
```

if the InfraQL binary is not in the system path you can explicitly specify this using the `exe` argument of the `InfraQL` constructor method, for example:

```python
from pyinfraql import InfraQL  
iql = InfraQL(exe='/some/other/path/infraql', keyfilepath='/tmp/infraql-demo.json')
```