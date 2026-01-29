import requests
from bs4 import BeautifulSoup as bs
import os
from urllib.parse import urlparse

def get_github_profile_image(username):
    """
    Ambil URL foto profil GitHub user dengan selector yang robust.
    Coba beberapa selector dan return URL jika ditemukan.
    """
    url = 'https://github.com/' + username
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        soup = bs(r.content, 'html.parser')
        
        # Coba selector 1: meta og:image (paling reliable)
        og_image = soup.find('meta', {'property': 'og:image'})
        if og_image and og_image.get('content'):
            return og_image['content']
        
        # Coba selector 2: link rel=image_src
        image_src = soup.find('link', {'rel': 'image_src'})
        if image_src and image_src.get('href'):
            return image_src['href']
        
        # Coba selector 3: .avatar-user img
        avatar = soup.find('img', {'class': 'avatar-user'})
        if avatar and avatar.get('src'):
            return avatar['src']
        
        # Fallback: selector 4: img alt=Avatar (original)
        profile_img = soup.find('img', {'alt': 'Avatar'})
        if profile_img and profile_img.get('src'):
            return profile_img['src']
        
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error jaringan: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def download_image(image_url, username):
    """
    Download gambar dari URL dan simpan dengan nama username.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(image_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Tentukan ekstensi file dari URL atau response header
        parsed_url = urlparse(image_url)
        ext = os.path.splitext(parsed_url.path)[1] or '.jpg'
        
        filename = f"{username}_profile{ext}"
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"Gambar berhasil disimpan: {filename}")
        return filename
    
    except Exception as e:
        print(f"Error download: {e}")
        return None

def main():
    print("=== GitHub Profile Image Scraper ===")
    github_user = input('Masukkan Username GitHub: ').strip()
    
    if not github_user:
        print("Username tidak boleh kosong!")
        return
    
    print(f"Mencari profil GitHub: {github_user}...")
    image_url = get_github_profile_image(github_user)
    
    if image_url:
        print(f"URL Foto Profil: {image_url}")
        
        # Tanya apakah user ingin download
        download_choice = input("Download gambar? (y/n): ").strip().lower()
        if download_choice == 'y':
            download_image(image_url, github_user)
    else:
        print(f"Foto profil tidak ditemukan untuk user: {github_user}")

if __name__ == '__main__':
    main()
