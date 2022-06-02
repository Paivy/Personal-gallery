#** Gallery app**

#### This is a simple Django program that allows a user to view various photos fro different locations. the user can search for photos according to their category and also copy the link to the photos url. photos acn also be viewed according to the loaction they were taken too.

\*\*\*## As users you can :

- View different photos that interest me.
- View different categories of photos.
- Copy a link to the photo to share with my friends.

---

\*\*\*## ~~Usage example~~

1. Open the website and browse the images.
2. If you see an image that interests you you can click on it to view it.\*\*\*

## Development setup

- To access the Code behind this site, you will need to:

1. Clone this repo:

```bash
git clone https://github.com/Paivy/Personal-gallery.git
```

2. Move to the folder and install requirements

```bash
cd gallery
pip install -r requirements.txt
```

3. Create database on psql shell

```SQL
psql
CREATE DATABASE gallery;
```

4. Migrate the database and run the application

```bash
python manage.py migrate
python manage.py runserver
```

## Technologies Used

- python3
- Django
- Jinja
- HTML
- Bootstrap
- css

## Known Bugs.

- There are currently no known bugs. If you experience any feel free to open an issue

### Support and contact details

If you have any queries regarding the my site, Please feel free to
contact on [gmail](paivyeshirera@gmail.com) and we will be happy to look
into your query
