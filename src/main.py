import sys
from get_transcript import get_captions
from gemini_api import generate, ask_question

def main():
    """
    Main function to process YouTube video URL, fetch its transcript,
    summarize it using Gemini API, and allow user to ask follow-up questions.
    """
    # Ensure correct number of arguments are passed
    if len(sys.argv) != 5:
        print("Usage: python main.py <YouTube URL> <Project Name> <Location> <Model Choice>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    project_name = sys.argv[2]
    location = sys.argv[3]
    model_choice = sys.argv[4]

    try:
        # Fetch the transcript from the YouTube video
        captions = get_captions(youtube_url)
        transcript = " ".join([entry['text'] for entry in captions])

        # Summarize the transcript using the Gemini API
        print("\nSummary:")
        generate(project_name, location, model_choice, transcript)

        # Enter into a loop for user to ask questions
        while True:
            question = input("\nEnter a question about the video transcript (or type 'exit' to quit): ")
            if question.lower() == 'exit':
                break
            print("\nAnswer:")
            ask_question(project_name, location, model_choice, question, transcript)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
