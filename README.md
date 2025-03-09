
## Hackathon - Python CSV Processor

---

### Problem statement brief

Create a Python script using only standard library modules to process multiple larger-than-memory CSV files in a folder.

---

### Details of files in input folder

- Folder can contain any number of csv files. Their size can range from 1 MB to 8 GB
- Each file includes a **header** row.
- Columns Details:
    - **city** (`str`): Length 4-20 characters
    - **temperature** (`float`): Ranges from **-20.00 to 60.00**
```
city,temperature
New York,23.62
Boston,25.00
New York,31.38
Seattle,17.28
Dallas,21.88
Denver,23.53
Houston,27.49
```

---

### **Task**

- Create a **single file** named `main.py` containing a function named process.
- `process` function should :
    - Take in **one argument**: the path to a folder where CSV files are stored.
    - Returns a **dictionary** with keys as cities names and dictionaries as values with **four metrics**: `count`, `avg`, `max`, and `min` of temperature column calculated for **all_cities**
      and for each **city**.
    - ```def process(folder_path: str) -> dict[str,dict]```

---

### **Example Output Dictionary**

```python
{
    'Boston': {'avg': 27.61, 'count': 4, 'max': 31.66, 'min': 23.5},
    'Chicago': {'avg': 24.74, 'count': 7, 'max': 33.77, 'min': 18.32},
    'Dallas': {'avg': 24.21, 'count': 3, 'max': 25.82, 'min': 21.88},
    'Denver': {'avg': 26.13, 'count': 5, 'max': 31.34, 'min': 18.36},
    'Houston': {'avg': 29.99, 'count': 2, 'max': 32.5, 'min': 27.49},
    'Los Angeles': {'avg': 22.98, 'count': 4, 'max': 30.17, 'min': 15.99},
    'Miami': {'avg': 30.75, 'count': 4, 'max': 33.69, 'min': 26.93},
    'New York': {'avg': 23.08, 'count': 4, 'max': 31.38, 'min': 19.43},
    'San Francisco': {'avg': 26.88, 'count': 4, 'max': 31.64, 'min': 20.0},
    'Seattle': {'avg': 22.51, 'count': 3, 'max': 33.78, 'min': 16.47},
    'all_cities': {'avg': 25.73, 'count': 40, 'max': 33.78, 'min': 15.99}
}
```
---
### **Conditions**
- Only Python standard library modules are allowed. No external packages should be used.
- Allowed Python Versions: **>= Python 3.10, <= Python 3.12**

---



### Evaluation Criteria

Your code will be tested on an **AWS EC2 Instance** with the following specifications:

- **Instance Type**: `t4g.medium`
- **vCPU**: 2
- **Memory**: 4 GiB
- **EBS Storage**: 32 GiB
- 4 Test folders with multiple csv files whose total sizes are:
    - **512 MB**
    - **2 GiB**
    - **4 GiB**
    - **8 GiB**

Ensure your solution is efficient and optimized for handling large CSV files in a memory-efficient way.

