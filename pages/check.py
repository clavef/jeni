# pages/check.py
import streamlit as st
import json
import pandas as pd
import zipfile
import io

st.title("📱 인스타 언팔체크")

st.markdown("""
**기능 설명**

인스타그램에서 받은 ZIP 파일을 업로드하면, 내가 팔로우하지만 나를 팔로우하지 않는 사람을 찾아줍니다.

1. 인스타그램에서 데이터 다운로드
2. 받은 ZIP 파일을 바로 업로드
3. 결과 확인 및 다운로드
""")

uploaded_zip = st.file_uploader("인스타그램 ZIP 파일 업로드", type="zip")

if uploaded_zip:
    try:
        with zipfile.ZipFile(uploaded_zip) as z:
            # followers_1.json 또는 followers.json 찾기
            followers_file = next((f for f in z.namelist() if "followers" in f and f.endswith(".json")), None)
            following_file = next((f for f in z.namelist() if "following" in f and f.endswith(".json")), None)

            if not followers_file or not following_file:
                st.error("ZIP 파일에서 followers 또는 following JSON 파일을 찾을 수 없습니다.")
            else:
                with z.open(followers_file) as f:
                    followers_data = json.load(f)
                with z.open(following_file) as f:
                    following_data = json.load(f)

                follower_usernames = set([
                    entry['string_list_data'][0]['value']
                    for entry in followers_data.get('relationships_followers', [])
                ])
                following_usernames = set([
                    entry['string_list_data'][0]['value']
                    for entry in following_data.get('relationships_following', [])
                ])

                not_following_back = sorted(list(following_usernames - follower_usernames))

                st.success(f"총 {len(not_following_back)}명이 나를 팔로우하지 않아요.")
                st.write(not_following_back)

                df = pd.DataFrame(not_following_back, columns=["Not Following Back"])
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("CSV로 다운로드", data=csv, file_name="not_following_back.csv", mime="text/csv")
    except Exception as e:
        st.error(f"처리 중 오류 발생: {e}")
