data = ({"id" : 4123, "name" : "EarthQuake"},
        {"id" : 4143, "name" : "Volcanic Eruption"},
        {"id" : 4121, "name" : "Mass Shooting"},
        {"id" : 4166, "name" : "Hurricane"},
        {"id" : 4187, "name" : "Extreme Heat Waves"},
        {"id" : 4133, "name" : "Distro"},
        {"id" : 4001, "name" : "Bistro"},

    )
disaster_event_data = ({
        "id":4133,
        "title": "Earth Quake in Nepal",
        "glide":"123A",
        "status": "alert",
        "description": "In May 2015, an EarthQuake struck Nepal. bleh",
        "date_occured": "12/13/2015",
        "date_ended": "12/15/2015",
        "disaster_type": "Earth Quake"
        },
        {
        "id":4135,
        "title": "Earth Quake in Haiti",
        "glide":"123B",
        "status": "current",
        "description": "In May 2014, an EarthQuake struck Haiti. bleh",
        "date_occured": "12/13/2014",
        "date_ended": "12/15/2014",
        "disaster_type": "Earth Quake"
        })
location_data = ({
        "id": 4123,
        "country": "Nepal",
        "state" : "Bagmati",
        "city" : "Kathmandu",
        "lat"  : None,
        "lon"   : None
},
{
        "id": 4124,
        "country": "Haiti",
        "state" : None,
        "city" : "Port au-Prince",
        "lat" : None,
        "lon" : None
})

victims_data = ({
        "location_id" : 4123,
        "num_deaths" : 13000,
        "num_missing" : 500,
        "num_injured" : 1400,
        "num_affected" : 34000
},
{
        "location_id" : 4124,
        "num_deaths" : 16000,
        "num_missing" : 900,
        "num_injured" : 10000,
        "num_affected" : 340000
})
