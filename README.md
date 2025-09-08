<h1 align="center" id="title">SpotiCode - Your Music Management Solution for Music Companies</h1>

<p id="description">Spoticode is a specialized Django-based web application designed exclusively for music companies that require robust tools to manage and organize their extensive music libraries. Whether you're a record label music publishing company or a music streaming service SpotiCode offers a comprehensive platform to streamline your music cataloging and curation processes. With SpotiCode music companies can effortlessly store and manage detailed information about albums, artists, songs, genres, and playlists enabling you to focus on what you do best - promoting and distributing exceptional music content to your audience.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Album Management: Efficiently store and organize albums by title release date and artist.
*   Artist Profiles: Create and manage detailed artist profiles including biographical information discography and more.
*   Song Catalog: Maintain a comprehensive catalog of songs with metadata and associated albums.
*   Genre Classification: Classify songs by genre to facilitate easy sorting searching and categorization.
*   Playlist Creation: Develop and manage curated playlists tailored to specific themes moods or promotional campaigns.

<h2>🛠️ Installation Steps:</h2>

<h5>1️⃣ Clone the Repository</h5>
<p>Clone the project repository to your local machine:</p>
```
git clone &lt;your-repo-url&gt;
```

<h5>2️⃣ Install Python Dependencies</h5>
<p>Open Command Prompt in your project folder and create a virtual environment:</p>
```
python -m venv venv
venv\Scripts\activate
```
<p>Then install all required packages:</p>
```
pip install -r requirements.txt
```

<h5>3️⃣ Create PostgreSQL Database</h5>
<p>Before running the app, create a PostgreSQL database. Open <code>psql</code> or PgAdmin and run:</p>
```
CREATE DATABASE your_db_name;
```

<h5>4️⃣ Configure Environment Variables</h5>
<p>Ensure your <code>.env</code> file contains the correct database connection info:</p>
```
DB_NAME=your_db_name
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

<h5>5️⃣ Apply Django Migrations</h5>
<p>Prepare the database schema:</p>
```
python manage.py makemigrations
python manage.py migrate
```

<h5>6️⃣ Run Extra Database Scripts</h5>
<p>Run the batch file <pre><code>update_db.bat</code></pre> provided in adjustments.</p>
<p>The batch file will ask for the database name, host, user, and password. If you leave the host empty, it will default to <code>localhost</code>, and if you leave the username empty, it will default to <code>postgres</code>.</p>

<h5>7️⃣ Create a Superuser (Optional)</h5>
<p>To access the Django admin panel:</p>
```
python manage.py createsuperuser
```

<h5>8️⃣ Run the Development Server</h5>
<p>Start the app using the provided batch file, which automatically activates the virtual environment and runs the server:</p>
```
SpotiCode.bat
```
<p>Access the app at <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></p>
