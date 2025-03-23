import requests
import random

# Function to get movie genres
def get_genres(api_key):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json()['genres']
        return {genre['id']: genre['name'] for genre in genres}
    else:
        print("Error fetching genres.")
        return {}

# Function to get movies by genre
def get_movies_by_genre(api_key, genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()['results']
        return movies
    else:
        print("Error fetching movies.")
        return []

# Main program
def main():
    api_key = "39d642a111703ede77d894a32e996736"  # Replace with your TMDB API key

    # Get available genres
    genres = get_genres(api_key)
    print("Available genres:")
    for genre_id, genre_name in genres.items():
        print(f"{genre_id}: {genre_name}")

    # Ask user for a genre
    genre_id = int(input("Enter the genre ID for your movie recommendation: "))

    # Get movies for the selected genre
    movies = get_movies_by_genre(api_key, genre_id)

    if movies:
        # Randomly select a movie
        recommended_movie = random.choice(movies)
        print(f"Recommended Movie: {recommended_movie['title']}")
        print(f"Overview: {recommended_movie['overview']}")
    else:
        print("No movies found for this genre.")

if __name__ == "__main__":
    main()