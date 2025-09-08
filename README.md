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

<h3>1️⃣ Clone the Repository</h3>
<p>Clone the project repository to your local machine:</p>
<pre><code>git clone https://github.com/desislava-pavlova/SpotiCode.git</code></pre>

<h3>2️⃣ Install Python Dependencies</h3>
<p>Open Command Prompt in your project folder and create a virtual environment:</p>
<pre><code>python -m venv venv
venv\Scripts\activate</code></pre>
<p>Then install all required packages:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>3️⃣ Create PostgreSQL Database</h3>
<p>Before running the app, create a PostgreSQL database. Open <code>psql</code> or PgAdmin and run:</p>
<pre><code>CREATE DATABASE your_db_name;</code></pre>

<h3>4️⃣ Configure Environment Variables</h3>
<p>Ensure your <code>.env</code> file contains the correct database connection info:</p>
<pre><code>DB_NAME=your_db_name
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432</code></pre>

<h3>5️⃣ Apply Django Migrations</h3>
<p>Prepare the database schema:</p>
<pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>

<h3>6️⃣ Run Extra Database Scripts</h3>
<p>Run the batch file <code>update_db.bat</code> provided in adjustments.</p>
<p>The batch file will ask for the database name, host, user, and password. If you leave the host empty, it will default to <code>localhost</code>, and if you leave the username empty, it will default to <code>postgres</code>.</p>

<h3>7️⃣ Create a Superuser (Optional)</h3>
<p>To access the Django admin panel:</p>
<pre><code>python manage.py createsuperuser</code></pre>

<h3>8️⃣ Run the Development Server</h3>
<p>Start the app using the provided batch file, which automatically activates the virtual environment and runs the server:</p>
<pre><code>SpotiCode.bat</code></pre>
<p>Access the app at <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></p>
