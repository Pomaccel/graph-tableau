import streamlit as st
import streamlit.components.v1 as components
import requests

# Set the page layout to 'wide' to reduce margins
st.set_page_config(layout="wide")

# Custom CSS to remove padding/margin from the left and right
st.markdown("""
    <style>
        .css-18e3th9 {  # Streamlit main content area
            padding-top: 1rem;
            padding-right: 0rem;
            padding-left: 0rem;
            padding-bottom: 1rem;
        }
        .css-1d391kg {  # Streamlit sidebar area
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title('Web Traffic Dashboard - Test by POM')

    # Tableau visualization details
    viz_url = "https://public.tableau.com/views/WebTrafficDashboard_17283124930700/KPICards"

    # Check if the Tableau URL is accessible
    try:
        response = requests.get(viz_url)
        if response.status_code == 200:
            st.success("Tableau visualization URL is accessible.")
        else:
            st.error(f"Error accessing Tableau URL. Status code: {response.status_code}")
            return
    except requests.RequestException as e:
        st.error(f"Error checking Tableau URL: {str(e)}")
        return

    # Embed the Tableau visualization using JavaScript API
    tableau_html = f"""
    <div id='tableauViz'></div>

    <script type='text/javascript' src='https://public.tableau.com/javascripts/api/tableau-2.min.js'></script>
    <script type='text/javascript'>
        var divElement = document.getElementById('tableauViz');
        divElement.style.width = '100%';  // Make sure the width spans the available space
        divElement.style.height = '850px';  // Set height to suit a desktop layout

        var vizElement = divElement.parentNode;
        vizElement.style.width = '100%';  // Ensure the parent container also stretches to full width
        vizElement.style.height = '850px';  // Set the height for better visibility on desktop

        var url = '{viz_url}';
        var options = {{
            hideTabs: false,
            hideToolbar: false,
            device: "desktop"  // This line ensures the view is for desktop
        }};
        var viz = new tableau.Viz(divElement, url, options);
    </script>
    """

    # Use the components function to render the HTML
    try:
        components.html(tableau_html, height=850, scrolling=True)
    except Exception as e:
        st.error(f"Error rendering Tableau visualization: {str(e)}")
        return

    st.write("This Web Traffic Dashboard is embedded from Tableau Public. If you don't see the dashboard, please check your internet connection and ensure that you can access Tableau Public.")

if __name__ == '__main__':
    main()
