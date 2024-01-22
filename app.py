import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests






with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu" ,
    options=["Home" , "Whatsapp Chat Analyzer" , "Contact"],
    icons=["house" , "whatsapp" , "envelope"],
    menu_icon="cast" , 
    default_index=0,)
if selected == "Home":
    with st.container():
        left_columns , right_column=st.columns(2)
        st.subheader("Welcome To :green[Whatsapp Chat Analyzer!!]")
        st.title("We Data Analyst Abhinav , Mayank and Vipul from HNBGU")
        st.subheader("We are passionate to give demo of our project")
        st.subheader("Synopsis")
        st.subheader("[Read more >](https://drive.google.com/file/d/1uhMPZG_aIYHkqUu4FanTKGJi-bIez24_/view?usp=sharing)")
        st.subheader("Report")
        st.subheader("[Read more >](https://drive.google.com/file/d/17Wm9avLeN0JetHsgB6T2dvPiyTqxqF6q/view?usp=sharing)")
        st.subheader("Presentation")
        st.subheader("[Read more >](https://drive.google.com/file/d/1MI3Mkc04__49E-DQWXxMtsmZNuRw6Gzn/view?usp=sharing)")
        
if selected == "Whatsapp Chat Analyzer":

    st.sidebar.title("Whatsapp Chat Analyzer")
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    if uploaded_file is not None:

        bytes_data = uploaded_file.getvalue()
        data = bytes_data.decode("utf-8")
        df = preprocessor.preprocess(data)

    # fetch unique users
        user_list = df['user'].unique().tolist()
        user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0,"Overall")

        selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

        if st.sidebar.button("Show Analysis"):

        # Stats Area
            num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user,df)
            st.title("Top Statistics")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.header("Total Messages")
                st.title(num_messages)
         
            with col3:
                st.header("Media Shared")
                st.title(num_media_messages)
            with col4:
                st.header("Links Shared")
                st.title(num_links)

        # monthly timeline
            st.title("Monthly Timeline")
            timeline = helper.monthly_timeline(selected_user,df)
            fig,ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'],color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # daily timeline
            st.title("Daily Timeline")
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # activity map
            st.title('Activity Map')
            col1,col2 = st.columns(2)

            with col1:
                st.header("Most busy day")
                busy_day = helper.week_activity_map(selected_user,df)
                fig,ax = plt.subplots()
                ax.bar(busy_day.index,busy_day.values,color='purple')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.header("Most busy month")
                busy_month = helper.month_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_month.index, busy_month.values,color='orange')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            st.title("Weekly Activity Map")
            user_heatmap = helper.activity_heatmap(selected_user,df)
            fig,ax = plt.subplots()
            ax = sns.heatmap(user_heatmap)
            st.pyplot(fig)

        # finding the busiest users in the group(Group level)
            if selected_user == 'Overall':
                st.title('Most Busy Users')
                x,new_df = helper.most_busy_users(df)
                fig, ax = plt.subplots()

                col1, col2 = st.columns(2)

                with col1:
                    ax.bar(x.index, x.values,color='red')
                    plt.xticks(rotation='vertical')
                    st.pyplot(fig)
                with col2:
                    st.dataframe(new_df)

            # WordCloud
            st.title("Wordcloud")
            df_wc = helper.create_wordcloud(selected_user,df)
            fig,ax = plt.subplots()
            ax.imshow(df_wc)
            st.pyplot(fig)

             # most common words
            most_common_df = helper.most_common_words(selected_user,df)

            fig,ax = plt.subplots()

            ax.barh(most_common_df[0],most_common_df[1])
            plt.xticks(rotation='vertical')

            st.title('Most commmon words')
            st.pyplot(fig)

        # emoji analysis
            emoji_df = helper.emoji_helper(selected_user,df)
            st.title("Emoji Analysis")

            col1,col2 = st.columns(2)

            with col1:
                st.dataframe(emoji_df)
            with col2:
                fig,ax = plt.subplots()
                ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f")
                st.pyplot(fig)
if selected == "Contact":
    st.header(":mailbox: Get In Touch With Me!")


    contact_form = """
    <form action="https://formsubmit.co/agg862646@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")










