## Docker build

`docker build . -t python:cst -f Dockerfile --no-cache`

### Docker Run

`docker run -it python:cst bash`

### Task1 

1. To Generate the raw data run below command

```
cd task1
python generate_data.py "input_raw_data.psv" 1000
```

2. To run the parser use below command

```
cd task1
python main.py input_raw_data.psv output.csv
```

### Task2

1. To Generate the raw data run below command

```
cd task2
python generate_data.py
```

2. To run the data anonymize process

```
cd task2
python main.py
```
