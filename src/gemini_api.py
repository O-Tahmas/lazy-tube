import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

def generate(project_name, location, model_choice, text):
    """
    Initializes the Vertex AI environment and generates a summary of the provided text.

    Args:
        project_name (str): The name of the Google Cloud project.
        location (str): The location of the Vertex AI resources.
        model_choice (str): The model to use for generating content.
        text (str): The text to be summarized.
    """
    vertexai.init(project=project_name, location=location)
    model = GenerativeModel(
        model_choice,
        system_instruction=[
            """You are a YouTube video summarizer. 
            Please summarize the video transcript that has been inserted in the prompt. 
            The user may also ask follow-up questions after this."""
        ],
    )
    responses = model.generate_content(
        [text],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

def ask_question(project_name, location, model_choice, question, transcript):
    """
    Initializes the Vertex AI environment and generates a response to the provided question
    based on the given transcript.

    Args:
        project_name (str): The name of the Google Cloud project.
        location (str): The location of the Vertex AI resources.
        model_choice (str): The model to use for generating content.
        question (str): The question to be answered.
        transcript (str): The transcript to base the answer on.
    """
    vertexai.init(project=project_name, location=location)
    model = GenerativeModel(
        model_choice,
        system_instruction=[
            """You are a YouTube video summarizer and Q&A assistant. 
            The user has already received a summary of the video transcript and may now ask follow-up questions."""
        ],
    )
    combined_text = f"Transcript: {transcript}\nQuestion: {question}"
    responses = model.generate_content(
        [combined_text],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

# Configuration for content generation
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0.5,
    "top_p": 0.95,
}

# Safety settings for content generation
safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}
