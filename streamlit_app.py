import streamlit as st
import streamlit.components.v1 as components
import requests

# Set the page layout to 'wide' to reduce margins
st.set_page_config(layout="wide")

# Custom CSS to handle responsive design for both mobile and desktop screens
st.markdown("""
    <style>
        .css-18e3th9 {  /* Streamlit main content area */
            padding-top: 1rem;
            padding-right: 0rem;
            padding-left: 0rem;
            padding-bottom: 1rem;
        }
        .css-1d391kg {  /* Streamlit sidebar area */
            display: none;
        }
        
        /* Media query for smaller screens (mobile devices) */
        @media (max-width: 768px) {
            #tableauViz {
                width: 100vw;
                height: 500px;
            }
        }
        
        /* Media query for larger screens (desktops) */
        @media (min-width: 769px) {
            #tableauViz {
                width: 100vw;
                height: 850px;
            }
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

        function adjustVizSize() {{
            if (window.innerWidth <= 768) {{
                // Mobile view
                divElement.style.width = '100vw';
                divElement.style.height = '500px';
            }} else {{
                // Desktop view
                divElement.style.width = '100vw';
                divElement.style.height = '850px';
            }}
        }}

        // Initial size adjustment
        adjustVizSize();

        // Adjust size on window resize
        window.addEventListener('resize', adjustVizSize);

        var url = '{viz_url}';
        var options = {{
            hideTabs: false,
            hideToolbar: false,
            device: window.innerWidth <= 768 ? "phone" : "desktop"
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
