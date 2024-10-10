from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_spotify_playlist(playlist_url):
    # Setup Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Runs the browser in headless mode
    
    # Correct initialization
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    
    # Open the Spotify playlist URL
    driver.get(playlist_url)
    
    # Wait for the page to load (you may need to adjust this time)
    time.sleep(5)  # Give time for the playlist to load
    
    # Extract the song titles and artists
    songs_list = []
    
    # Each track item
    song_elements = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="tracklist-row"]')
    
    for song_element in song_elements:
        # Get song name
        song_name = song_element.find_element(By.CSS_SELECTOR, 'span[data-testid="track-name"]').text
        
        # Get artist names
        artist_element = song_element.find_element(By.CSS_SELECTOR, 'a[data-testid="track-artist"]')
        artist_name = artist_element.text
        
        songs_list.append((song_name, artist_name))
    
    driver.quit()  # Close the browser
    
    return songs_list

# Example usage
playlist_url = "https://open.spotify.com/playlist/6zVe5DNZgP8F9VgWzQu0HL?si=AgMjNO6uSNi0bND8Xjr12g&pi=a-7ZBnnt5TSHa8"
songs = scrape_spotify_playlist(playlist_url)

if songs:
    print(f"Found {len(songs)} songs:")
    for idx, (song, artist) in enumerate(songs, start=1):
        print(f"{idx}. {song} by {artist}")
else:
    print("No songs found or unable to scrape the playlist.")
