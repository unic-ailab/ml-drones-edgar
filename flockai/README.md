## Instructions

Copy the sensor files line_acceleration.py and velocity.py to the sensors folder found where the flockai library is installed.
So, it should look something like this C:/path/to/webots/lib/controller/<your_python_version>/flockai/models/sensors.

On webots, create a new controller and copy the contents from modified_mavic2dji_lin_reg.py.

Go to the folder where the new controller was created and copy the data folder from this repo as well as the model.sav file you
want to use

When choosing a model, change the filename variable from modified_mavic2dji_lin_reg.py to what the model is called.

Now, you should be able run the world.
