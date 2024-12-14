import streamlit as st
import base64

def app():
    st.markdown("### Tableau Dashboard")

    # Open the file as binary
    try:
        # Goto Tableau
        st.markdown(
            f'<a href="https://public.tableau.com/views/DSMLBootcampProjectI-DemoData/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link" target="_blank" rel="noopener noreferrer" style="text-decoration:none;">'
            f'<button style="background-color:LightBlue; color:black; border-radius:5px; padding:10px 20px;">View in Tableau Public</button>'
            f'</a>',
            unsafe_allow_html=True,
        )
        # Create an IFrame
        html_code = "<div class='tableauPlaceholder' id='viz1734172657285' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DS&#47;DSMLBootcampProjectI-DemoData&#47;Dashboard1&#47;1_rss.png' style='border: none,height:20vh;' /></a></noscript><object class='tableauViz'  style='display:none;height:10vh;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DSMLBootcampProjectI-DemoData&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DS&#47;DSMLBootcampProjectI-DemoData&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1734172657285');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.65)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1927px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);</script>"
        
        st.components.v1.html(html_code, height=850)
        
      
    except FileNotFoundError:
        st.error("PDF File Not Found.")
    except Exception as e:
        st.error(f"Error: {e}")
    