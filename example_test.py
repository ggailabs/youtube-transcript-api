import sys
from youtube_transcript_api import YouTubeTranscriptApi


def main(video_id: str) -> None:
    """Simple script to fetch and display a transcript."""
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)
    for snippet in transcript:
        print(f"{snippet.start:.2f}\t{snippet.duration:.2f}\t{snippet.text}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python example_test.py <video_id>")
        sys.exit(1)
    main(sys.argv[1])
