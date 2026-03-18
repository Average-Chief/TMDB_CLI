from argparse import ArgumentParser
from rich import print 
from api import fetch_movies

def main():
    parser = ArgumentParser(description="TMDB CLI Tool")
    parser.add_argument(
        "--type",
        type = str,
        required=True,
        choices = ["playing", "upcoming", "top", "popular"],
        help='Type of movies to fetch: "playing", "upcoming", "top", or "popular"',
    )
    args = parser.parse_args()

    try: 
        movies = fetch_movies(args.type)
        print("\n🎬 [bold cyan]Movies:[/bold cyan]\n")
        for i, movie in enumerate(movies[:10], 1):
            print(f"{i}. {movie}")
    except Exception as e:
        print(f"[bold red]Error:[/bold red] {e}")

if __name__=="__main__":
    main()