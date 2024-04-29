PROJECT TITLE: Nts’oekhe Distributed Database
DESCRIPTION:
This project is a distributed database management system, Nts’oekhe, that can be used in healthcare facilities to enable secure, efficient handling and storage of health-related data digitally. 
How to install and run the project:
* User needs to have Django version 5.0.4.
* User should use command prompt and activate virtual environment then run the code through virtual environment.
* Run servers on different ports because having data at different places, the data on a certain node shall be distinguished by the IP address. 
Installation process:
1. Create a virtual environment (optional but recommended):
      python -m venv myenv
2. Activate the virtual environment:
* On Windows
			myenv\Scripts\activate
* On linux
			source myenv/bin/activate
3. Start the development server
      python manage.py runserver
