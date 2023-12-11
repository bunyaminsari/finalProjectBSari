### INF601 - Advanced Programming with Python
#### Bunyamin Sari
#### finalProjectBSari

## Description
Cyber+ App utilizes [NetDetective API](https://rapidapi.com/tomwimmenhove/api/netdetective) which is an easy-to-use API that provides information about an IP address, including, but not limited to, whether it’s known for spam, brute-force attacks, bot-nets, VPN endpoints, data center endpoints, and more.

With the help of the DetectiveIP API, you can quickly and easily gather information about any IP address to help filter requests and avoid potential attacks.

## API Access Key
Create an account at [Rapid API](https://rapidapi.com). Once the account has been set up, subscribe to [NetDetective API](https://rapidapi.com/tomwimmenhove/api/netdetective) and get your access key. Create a python file as "api_keys.py" in the directory of your app, not project. Paste your API access key in the "api_keys.py" file as shown below:
```
NETDETECTIVE_API_KEY = 'YOUR_API_ACCESS_KEY'
```

## Pip Install Instructions
Please run the following: 
```
pip install -r requirements.txt
```
## Create SQL entries for the database
This will create any SQL entries that need to go into the database. In a terminal windows, please type the following:
```
python manage.py makemigrations
```
## Apply the Migrations
This will apply the migrations. In a terminal windows, please type the following:
```
python manage.py migrate
```
## Create Super User
This will create the administrator login for your /admin side of your project. In a terminal windows, please type the following:
```
python manage.py createsuperuser
```
## Run the Development Server:
You can start the development server using the following command:
```
python manage.py runserver
```

