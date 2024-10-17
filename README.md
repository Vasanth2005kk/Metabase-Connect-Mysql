Prerequisites:

    Metabase installed

    MySQL instance : You should have access to a MySQL database with its credentials (host, port, database name, username, password).


 Metabase installed
		
		Step-by-Step Guide to Install Metabase on Linux

		1. Install Java (Metabase requires Java):

			
			sudo apt update
			sudo apt install openjdk-11-jdk

			Verify the installation: 
				 java -version

		2. Download Metabase:
		
		Go to the Metabase download page and get the link for the latest JAR file, or use the following command to download it directly:

			wget https://downloads.metabase.com/v0.46.6/metabase.jar

		3. Run Metabase:

			After downloading the JAR file, you can run Metabase using the following command:

				java -jar metabase.jar

			By default, Metabase will run on port 3000. 
			You can access it via "http://localhost:3000" in your browser.

		4: Connect MySQL Database to Metabase

			1. Open Metabase in your browser. If it's running locally, go to:

			   ```
			   http://localhost:3000
			   ```

			2. Once Metabase is running, go to **Settings**:

			   - Click the **gear icon** (⚙️) in the upper-right corner.
			   - Click **Admin** > **Databases**.

			3. Click **Add a Database**.

			4. Fill in the connection details for your MySQL database:

			   Database Type	: Select **MySQL**.

			   Name				: Give your database a name (e.g., "My Local MySQL").
			   
			   Host				: Enter `localhost` (since you are connecting to a local MySQL instance).
			   
			   Port				: The default MySQL port is (3306).
			   
			   Database 		: Enter the name of your database (e.g., `metabase_db`).
			   
			   Username			: Enter the MySQL username (e.g., `metabase_user`).
			   
			   Password			: Enter the password for your MySQL user.
			   
			   SSL				: If you are connecting locally and don’t need SSL, leave this unchecked.

			5. Click (Save).

			Metabase will now try to connect to the MySQL database. If everything is set up correctly, Metabase will show a success message, and the MySQL database will be available in your list of data sources.

#Metabase analysis image

![Metabase analysis image][movielens.png]