import argparse

from youtube_transcript_api import YouTubeTranscriptApi


def main(video_id: str, languages: list[str]) -> None:
    """Simple script to fetch and display a transcript."""
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id, languages)
    for snippet in transcript:
        print(f"{snippet.start:.2f}\t{snippet.duration:.2f}\t{snippet.text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch a video's transcript using youtube-transcript-api"
    )
    parser.add_argument("video_id", help="YouTube video ID")
    parser.add_argument(
        "-l",
        "--languages",
        nargs="*",
        default=["en"],
        help="Preferred language codes (e.g. 'en', 'pt').",
    )
    args = parser.parse_args()
    main(args.video_id, args.languages)
