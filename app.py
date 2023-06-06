import openai
import streamlit as st

# Set up OpenAI API credentials
openai.api_key = "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"

# Define GPT-3 model
model_engine = "davinci:ft-personal-2023-04-29-21-25-53"

# Define default parameters for the API call
def_params = {
    "model": model_engine,
    "temperature": 0.5,
    "max_tokens": 1024,
    "frequency_penalty": 2.0,

}

# Define Streamlit app
def app():
    # Set app title and description
    st.set_page_config(page_title="Blog Generator", page_icon=":memo:", layout="wide")
    st.title("Blog Generator")
    st.write("Enter your blog topic and we'll generate a blog post for you!")
    
    # Define input box
    prompt = st.text_input("Enter your blog topic here:")
    # st.markdown('<div style={{ height: "600px", width: "400px" }}><iframe src={`https://ora.sh/embed/a84f2a85-dde8-4e9c-80ed-9c2dc6438406`} width="100%" height="100%" style={{ border: "0", borderRadius: "4px" }}/></div>', unsafe_allow_html=True)
    
    # Define button to trigger API call and blog generation
    if st.button("Generate Blog"):
        # Call OpenAI API to generate blog post
        params = def_params.copy()
        params["prompt"] = prompt
        response = openai.Completion.create(**params)
        
        # Extract generated blog post from API response
        blog_post = response.choices[0].text
        
        # Display generated blog post
        st.write(blog_post)
        
        # markdown with unsafe allows us to display HTML

# Run app
if __name__ == "__main__":
    app()