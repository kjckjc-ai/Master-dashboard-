
import streamlit as st
import pandas as pd
from thefuzz import process
from io import BytesIO
import os
import plotly.express as px

# Custom wide layout for Streamlit Cloud
st.markdown("""
    <style>
        .main {
            max-width: 95%;
            padding-left: 2rem;
            padding-right: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

def authenticate(username, password):
    USERS = {"admin": "pass123", "user": "school2024"}
    return USERS.get(username) == password
    pass
    pass

@st.cache_data
def load_data():
    df = pd.read_csv("National datasheeet.csv")
    df['SchoolWebsite'] = df['SchoolWebsite'].apply(lambda x: "http://" + x if isinstance(x, str) and not x.startswith("http") else x)
    return df
    pass
    pass

df = load_data()

with st.sidebar:
    st.title("Login")
    uname = st.text_input("Username", key="auth_user")
    pword = st.text_input("Password", type="password", key="auth_pass")
    if not authenticate(uname, pword):
        st.warning("Please enter valid credentials.")
        st.stop()
    else:
        st.success("Logged in")

tab1, tab2 = st.tabs(["Trust Overview", "National View"])


with tab2:
    national_data = pd.read_csv('National datasheeet.csv')
    national_data['SchoolWebsite'] = national_data['SchoolWebsite'].apply(lambda x: 'http://' + x if isinstance(x, str) and not x.startswith('http') else x)
    st.subheader('National View (from CSV)')
    st.write(national_data.head())
    from datetime import datetime
    
    # Set page configuration
    def load_phase_summary(filters=None):
        pass
    def load_religion_summary(filters=None):
        pass
    def load_gender_summary(filters=None):
        pass
    def load_local_authorities():
        pass
    def load_establishment_types():
        pass
    def load_establishment_groups():
        pass
    def load_phases():
        pass
    def load_trusts():
        pass
    def load_genders():
        pass
    def load_religions():
        pass
    def load_all_school_names():
        pass
    def load_all_trust_names():
        pass
    def find_similar_schools(search_term, all_schools, limit=5):
        """Find similar school names using simple string matching"""
        if not search_term:
            return []
    pass
    pass
    pass
    pass
        
    search_term = search_term.lower()
        
        # Get all school names as a list
        school_names = all_schools['EstablishmentName'].tolist()
        
        # Find schools that contain the search term
        matches = [name for name in school_names if search_term in name.lower()]
        
        # If we don't have enough matches, try more flexible matching
        if len(matches) < limit:
            # Split search term into words
            search_words = search_term.split()
            
            # Find schools that contain any of the search words
            for word in search_words:
                if len(word) > 2:  # Only use words with more than 2 characters
                    word_matches = [name for name in school_names if word in name.lower()]
                    for match in word_matches:
                        if match not in matches:
                            matches.append(match)
                            if len(matches) >= limit:
                                break
                    if len(matches) >= limit:
                        break
        
        return matches[:limit]
    
    def find_similar_trusts(search_term, all_trusts, limit=5):
        """Find similar trust names using simple string matching"""
        if not search_term:
            return []
    pass
    pass
        
        search_term = search_term.lower()
        
        # Get all trust names as a list
        trust_names = all_trusts['Trusts (name)'].tolist()
        
        # Find trusts that contain the search term
        matches = [name for name in trust_names if search_term in name.lower()]
        
        # If we don't have enough matches, try more flexible matching
        if len(matches) < limit:
            # Split search term into words
            search_words = search_term.split()
            
            # Find trusts that contain any of the search words
            for word in search_words:
                if len(word) > 2:  # Only use words with more than 2 characters
                    word_matches = [name for name in trust_names if word in name.lower()]
                    for match in word_matches:
                        if match not in matches:
                            matches.append(match)
                            if len(matches) >= limit:
                                break
                    if len(matches) >= limit:
                        break
        
        return matches[:limit]
    
    @st.cache_data
    def search_schools(name="", trust_name="", la="", establishment_groups=None, phase="", postcode="", gender="", religion="", show_all=False, page=1, per_page=20):
    def get_school_details(urn):
    def get_trust_schools(trust_name):
    def load_summary_stats(filters=None):
    def create_school_types_chart(data):
        fig = px.pie(
            data, 
            values='Count', 
            names='EstablishmentTypeGroup',
            title='School Types Distribution',
            hole=0.4,
        fig.update_layout(margin=dict(t=30, b=0, l=0, r=0))
        fig.update_traces(
            hoverinfo='label+percent+value',
            textinfo='label+value',
            textfont_size=12,
        return fig
    pass
    pass
    
    def create_phase_chart(data):
        fig = px.bar(
            data, 
            x='PhaseOfEducation', 
            y='Count',
            title='Phase of Education',
            color='PhaseOfEducation',
            labels={'PhaseOfEducation': 'Phase', 'Count': 'Number of Schools'}
        fig.update_layout(margin=dict(t=30, b=0, l=0, r=0), xaxis_tickangle=-45)
        return fig
    pass
    pass
    
    def create_religion_chart(data):
        fig = px.pie(
            data, 
            values='Count', 
            names='ReligiousCharacter',
            title='Religious Character',
            hole=0.4,
        fig.update_layout(margin=dict(t=30, b=0, l=0, r=0))
        fig.update_traces(
            hoverinfo='label+percent+value',
            textinfo='label+value',
            textfont_size=12,
        return fig
    pass
    pass
    
    def create_gender_chart(data):
        fig = px.pie(
            data, 
            values='Count', 
            names='Gender',
            title='Gender Distribution',
            hole=0.4,
        fig.update_layout(margin=dict(t=30, b=0, l=0, r=0))
        fig.update_traces(
            hoverinfo='label+percent+value',
            textinfo='label+value',
            textfont_size=12,
        return fig
    pass
    pass
    
    # Function to create a direct HTML component for the infographic
    def create_infographic_component(school_details):
        # Convert school details to the format expected by the infographic generator
        school_data = {
            "name": school_details['EstablishmentName'],
            "urn": str(school_details['URN']),
            "category": school_details['TypeOfEstablishment (name)'],
            "address": school_details['FullAddress'],
            "schoolCapacity": str(int(school_details['SchoolCapacity'])),
            "numberOfPupils": str(int(school_details['NumberOfPupils'])),
            "fsmPercentage": str(school_details['PercentageFSM']),
            "schoolType": school_details['EstablishmentTypeGroup (name)'],
            "phaseOfEducation": school_details['PhaseOfEducation (name)'],
            "headTeacher": school_details['HeadTeacherFullName'],
            "laName": school_details['LA (name)']
        }
    pass
    pass
        
        # Convert the school data to a JSON string for JavaScript
        school_data_json = str(school_data).replace("'", '"')
        
        # Create the HTML for the infographic
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                }}
                
                body {{
                    background-color: #f5f5f7;
                    color: #1d1d1f;
                    line-height: 1.5;
                }}
                
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                
                .infographic {{
                    background-color: white;
                    border-radius: 20px;
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
                    padding: 40px;
                    margin-bottom: 30px;
                    overflow: hidden;
                }}
                
                .infographic-header {{
                    text-align: center;
                    margin-bottom: 30px;
                }}
                
                .school-name {{
                    font-size: 32px;
                    font-weight: 600;
                    margin-bottom: 10px;
                    color: #1d1d1f;
                }}
                
                .school-details {{
                    font-size: 16px;
                    color: #86868b;
                    margin-bottom: 5px;
                }}
                
                .rating-container {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin: 30px 0;
                }}
                
                .rating-circle {{
                    width: 150px;
                    height: 150px;
                    border-radius: 50%;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    color: white;
                    font-weight: 600;
                    background: linear-gradient(135deg, #42a1ec, #0070c9);
                    box-shadow: 0 4px 15px rgba(0, 112, 201, 0.2);
                }}
                
                .rating-label {{
                    font-size: 14px;
                    margin-bottom: 5px;
                }}
                
                .rating-value {{
                    font-size: 28px;
                }}
                
                .metrics-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                    gap: 20px;
                    margin: 30px 0;
                }}
                
                .metric-card {{
                    background-color: #f5f5f7;
                    border-radius: 12px;
                    padding: 20px;
                    text-align: center;
                }}
                
                .metric-title {{
                    font-size: 14px;
                    color: #86868b;
                    margin-bottom: 10px;
                }}
                
                .metric-value {{
                    font-size: 24px;
                    font-weight: 600;
                    color: #1d1d1f;
                }}
                
                .section-title {{
                    font-size: 20px;
                    font-weight: 600;
                    margin: 30px 0 15px;
                    color: #1d1d1f;
                }}
                
                .highlights-container {{
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                    gap: 20px;
                    margin: 20px 0;
                }}
                
                .highlight-card {{
                    background-color: #f5f5f7;
                    border-radius: 12px;
                    padding: 20px;
                }}
                
                .highlight-title {{
                    font-size: 16px;
                    font-weight: 600;
                    margin-bottom: 10px;
                    color: #1d1d1f;
                }}
                
                .highlight-list {{
                    list-style-type: none;
                }}
                
                .highlight-item {{
                    margin-bottom: 10px;
                    font-size: 14px;
                    color: #515154;
                    position: relative;
                    padding-left: 20px;
                }}
                
                .highlight-item:before {{
                    content: "•";
                    color: #0070c9;
                    font-size: 18px;
                    position: absolute;
                    left: 0;
                    top: -2px;
                }}
                
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    font-size: 12px;
                    color: #86868b;
                }}
                
                .download-btn {{
                    display: inline-block;
                    background: linear-gradient(135deg, #42a1ec, #0070c9);
                    color: white;
                    font-weight: 600;
                    padding: 12px 24px;
                    border-radius: 30px;
                    text-decoration: none;
                    margin-top: 20px;
                    box-shadow: 0 4px 10px rgba(0, 112, 201, 0.2);
                    transition: all 0.3s ease;
                    cursor: pointer;
                }}
                
                .download-btn:hover {{
                    transform: translateY(-2px);
                    box-shadow: 0 6px 15px rgba(0, 112, 201, 0.3);
                }}
                
                /* Responsive adjustments */
                @media (max-width: 768px) {{
                    .infographic {{
                        padding: 20px;
                    }}
                    
                    .metrics-grid,
                    .highlights-container {{
                        grid-template-columns: 1fr;
                    }}
                    
                    .school-name {{
                        font-size: 24px;
                    }}
                    
                    .rating-circle {{
                        width: 120px;
                        height: 120px;
                    }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div id="infographic" class="infographic">
                    <!-- Infographic content will be generated here -->
                </div>
                
                <div style="text-align: center;">
                    <button id="downloadBtn" class="download-btn">Download Infographic</button>
                </div>
            </div>
    
            <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
            
            <script>
                // Function to generate the infographic based on school data
                function generateInfographic(schoolData) {{
                    const infographicEl = document.getElementById('infographic');
                    
                    // Format capacity utilization
                    const capacityUtilization = schoolData.numberOfPupils && schoolData.schoolCapacity 
                        ? Math.round((parseInt(schoolData.numberOfPupils) / parseInt(schoolData.schoolCapacity)) * 100) 
                        : 0;
                    
                    // Determine rating color based on FSM percentage
                    let ratingColor = 'linear-gradient(135deg, #42a1ec, #0070c9)'; // Default blue
                    let ratingText = 'Average';
                    
                    const fsmPercentage = parseFloat(schoolData.fsmPercentage) || 0;
                    
                    if (fsmPercentage > 30) {{
                        ratingColor = 'linear-gradient(135deg, #ff5e3a, #ff2d55)'; // Red
                        ratingText = 'High FSM';
                    }} else if (fsmPercentage > 20) {{
                        ratingColor = 'linear-gradient(135deg, #ffcc00, #ff9500)'; // Orange
                        ratingText = 'Medium FSM';
                    }} else if (fsmPercentage < 10) {{
                        ratingColor = 'linear-gradient(135deg, #34c759, #30b94d)'; // Green
                        ratingText = 'Low FSM';
                    }}
                    
                    // Build the HTML for the infographic
                    const html = `
                        <div class="infographic-header">
                            <h1 class="school-name">${{schoolData.name}}</h1>
                            <p class="school-details">${{schoolData.category || 'School'}}</p>
                            <p class="school-details">${{schoolData.address || ''}}</p>
                            <p class="school-details">URN: ${{schoolData.urn || 'N/A'}}</p>
                        </div>
                        
                        <div class="rating-container">
                            <div class="rating-circle" style="background: ${{ratingColor}}">
                                <span class="rating-label">FSM Percentage</span>
                                <span class="rating-value">${{fsmPercentage}}%</span>
                                <span class="rating-label">${{ratingText}}</span>
                            </div>
                        </div>
                        
                        <h2 class="section-title">Key Metrics</h2>
                        <div class="metrics-grid">
                            <div class="metric-card">
                                <p class="metric-title">School Capacity</p>
                                <p class="metric-value">${{schoolData.schoolCapacity || 'N/A'}}</p>
                            </div>
                            <div class="metric-card">
                                <p class="metric-title">Number of Pupils</p>
                                <p class="metric-value">${{schoolData.numberOfPupils || 'N/A'}}</p>
                            </div>
                            <div class="metric-card">
                                <p class="metric-title">Capacity Utilization</p>
                                <p class="metric-value">${{capacityUtilization}}%</p>
                            </div>
                            <div class="metric-card">
                                <p class="metric-title">FSM Percentage</p>
                                <p class="metric-value">${{fsmPercentage}}%</p>
                            </div>
                        </div>
                        
                        <div class="highlights-container">
                            <div class="highlight-card">
                                <h3 class="highlight-title">School Information</h3>
                                <ul class="highlight-list">
                                    <li class="highlight-item">School Type: ${{schoolData.schoolType || 'N/A'}}</li>
                                    <li class="highlight-item">Phase of Education: ${{schoolData.phaseOfEducation || 'N/A'}}</li>
                                    <li class="highlight-item">Local Authority: ${{schoolData.laName || 'N/A'}}</li>
                                    <li class="highlight-item">Head Teacher: ${{schoolData.headTeacher || 'N/A'}}</li>
                                </ul>
                            </div>
                        </div>
                        
                        <div class="footer">
                            <p>Data from Get Information about Schools service</p>
                            <p>Generated on ${{new Date().toLocaleDateString()}}</p>
                        </div>
                    `;
                    
                    // Set the HTML content
                    infographicEl.innerHTML = html;
                }}
                
                // Initialize with the provided data
                const schoolData = {school_data_json};
                generateInfographic(schoolData);
                
                // Set up download button
                document.getElementById('downloadBtn').addEventListener('click', function() {{
                    html2canvas(document.getElementById('infographic')).then(canvas => {{
                        const link = document.createElement('a');
                        link.download = `${{schoolData.name.replace(/[^a-z0-9]/gi, '_').toLowerCase()}}_infographic.png`;
                        link.href = canvas.toDataURL('image/png');
                        link.click();
                    }});
                }});
            </script>
        </body>
        </html>
        """
        
        return html_content
    
    # Main app
    def main():
        # Initialize session state for filters
        if 'filters' not in st.session_state:
            st.session_state.filters = {
                'name': '',
                'trust_name': '',
                'la': '',
                'establishment_groups': [], # Changed from school_types to establishment_groups
                'phase': '',
                'postcode': '', # Kept as postcode (from fixed_app.py)
                'gender': '',
                'religion': '',
                'show_all': False
            }
    pass
    pass
        
        # Initialize pagination
        if 'page' not in st.session_state:
            st.session_state.page = 1
        
        # Load data
            default=st.session_state.filters['establishment_groups']
        
        # Phase filter
        phase_options = [""] + phases["PhaseOfEducation (name)"].tolist()
        phase_filter = st.sidebar.selectbox(
            "Phase of Education",
            phase_options,
            index=phase_options.index(st.session_state.filters['phase']) if st.session_state.filters['phase'] in phase_options else 0
        
        # Postcode filter (kept as in fixed_app.py)
        postcode_filter = st.sidebar.text_input("Postcode (starts with)", value=st.session_state.filters['postcode'])
        
        # Gender filter
        gender_options = [""] + genders["Gender (name)"].tolist()
        gender_filter = st.sidebar.selectbox(
            "Gender",
            gender_options,
            index=gender_options.index(st.session_state.filters['gender']) if st.session_state.filters['gender'] in gender_options else 0
        
        # Religious character filter
        religion_options = [""] + religions["ReligiousCharacter (name)"].tolist()
        religion_filter = st.sidebar.selectbox(
            "Religious Character",
            religion_options,
            index=religion_options.index(st.session_state.filters['religion']) if st.session_state.filters['religion'] in religion_options else 0
        
        # Show all results option
        show_all_results = st.sidebar.checkbox("Show all results (may be slow)", value=st.session_state.filters['show_all'])
        
        # Apply filters button
        if st.sidebar.button("Apply Filters"):
            st.session_state.filters = {
                'name': name_filter,
                'trust_name': trust_filter,
                'la': la_filter,
                'establishment_groups': group_filter, # Changed from school_types to establishment_groups
                'phase': phase_filter,
                'postcode': postcode_filter, # Kept as postcode (from fixed_app.py)
                'gender': gender_filter,
                'religion': religion_filter,
                'show_all': show_all_results
            }
            # Reset pagination when filters change
            st.session_state.page = 1
            
        # Reset filters button
        if st.sidebar.button("Reset Filters"):
            st.session_state.filters = {
                'name': '',
                'trust_name': '',
                'la': '',
                'establishment_groups': [], # Changed from school_types to establishment_groups
                'phase': '',
                'postcode': '', # Kept as postcode (from fixed_app.py)
                'gender': '',
                'religion': '',
                'show_all': False
            }
            # Reset pagination when filters change
            st.session_state.page = 1
            # Rerun to update the UI
            st.rerun()
        
        # Main content
        st.title("England Schools Dashboard")
        
        # Get current filters
        current_filters = st.session_state.filters
        
        # Load data with current filters
