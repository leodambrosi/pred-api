# pred-api
Example of simple deployment of linear regression model via rest api flask on heroku

Create app in Heroku and follow the instructions on https://dashboard.heroku.com/apps/<app-name>/deploy/heroku-git

````
# initialize
$ heroku login
$ heroku git:clone -a pred-api
$ cd pred-api

# add files and commit
$ git add .
$ git commit -am "make it better"
$ git push heroku master
````

Execute

````
curl https://pred-api.herokuapp.com/predict -H application/json --data-binary '{ "crime_rate": 0.1, "avg_number_of_rooms": 4.0, "distance_to_employment_centers": 6.5, "property_tax_rate": 330.0, "pupil_teacher_ratio": 19.5 }'
````

It returns
```
{"house_value":6.3,"stddev":5.1}
```

Debugging
````
$ heroku logs
````