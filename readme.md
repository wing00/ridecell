Using django-filters & django-rest-gis

private location endpoint
/add_location/

public location endpoint
/location/?dist=<radius>&point=<long>,<lat>
/location/?dist=1&point=10,10

private reservation endpoint
/parking_spot/

public  reservation endpoint
/reserve_spot/<id>/

curl -XPATCH -H "Content-type: application/json" -d '{"start_time":"2018-04-12T01:01:00Z", "end_time":"2018-04-12T01:01:00Z"}' http://localhost:8000/reserve_spot/11/

TO DO:
validation for start and end times
permissions for public/private 
delete reservation