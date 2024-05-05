## Step 1: install XAMPP and run mysql on port 3306
## Step 2: create python env with deps
```
    conda create --name capstone python=3.10
    conda activate capstone
    conda install flask conda-forge::mysql-connector-python
```
## Step 3: initialize database and populate with products
```
    cd ecommerce\server
    python .\db-init\db-setup.py
```
## Step 4: run application
```
    flask --app server run
```