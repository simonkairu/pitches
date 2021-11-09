# Pitches 

## AURTHOR 
Simon Kairu

## DESCRIPTION 
 - This is a Python-Flask Application that allows users to create one minute pitch. You only have 60 seconds to impress someone. 1 minute can make or break you.
The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

## User Story

- Users can see the pitches other people have posted.

- Users can vote on the pitch they liked and give it a downvote or upvote.

- Users can sign in to leave a comment.

- Users can register on the website.

- Users can view the pitches they have created in their profile page..

- Users can comment on the different pitches and leave feedback. 

- Users can submit a pitch in any category. 

- Users can view the different categories. 

## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/simonkairu/pitches.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd pitches
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `http://127.0.0.1:5000/`.

## Technologies used 
1.python3.8 <br>
2.Heroku <br>
3.Bootstrap <br>
4.HTML <br>
5.css <br>
6.Flask

## Known Bugs 
No known bugs <br>
Report bugs:|simonkairu14@gmail.com
