This file is for you to describe the project application. Typically
you would include information such as the information below:

Installation and Setup
======================

Install ``project`` using the setup.py script::

    $ cd project
    $ python setup.py develop

Create the project database for any model classes defined::

    $ gearbox setup-app

Start the paste http server::

    $ gearbox serve

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ gearbox serve --reload --debug

Then you are ready to go.

Startup after setting up for first time
tg2env\Scripts\activate (Windows)
cd NOMAD\project
gearbox serve --reload --debug
